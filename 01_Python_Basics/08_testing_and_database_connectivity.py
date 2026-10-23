"""
Python Unit Testing and Database Connections - Study Reference

Topics covered:
    1.  Unit testing basics with unittest (test cases, assertions, exceptions, subTest)
    2.  Database connection basics with sqlite3 (connect, execute, fetch, commit, rollback)
    3.  Applying both: a small repository class that talks to the database
    4.  Testing database code with an in-memory database (setUp / tearDown)
    5.  Testing without a real database using mocks (unittest.mock)
    6.  How to run the tests, and how this applies to MySQL / PostgreSQL

Everything here uses only the standard library, so the file runs as-is:
    python 08_unit_testing_and_databases.py

Note: sample outputs are written as `# --> ...`.
"""

import sqlite3
import unittest
from unittest.mock import MagicMock, patch


#========================
# Part 1: Unit Testing Basics - Code Under Test
#========================
# A unit test checks ONE small piece of code (a "unit", usually a function or
# method) in isolation and reports whether it behaves as expected.
# Tests are valuable because they catch bugs early and make refactoring safe.
def add(a, b):
    """Return the sum of a and b."""
    return a + b


def divide(a, b):
    """Return a / b, raising ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


#========================
# Part 1: Writing Test Cases (unittest.TestCase)
#========================
# Rules of thumb:
#   - Put tests in a class that inherits from unittest.TestCase.
#   - Every test method name must start with "test" or it will not run.
#   - Each test calls the code and checks the result with an assertion.
#   - Tests must be independent: no test may rely on another one.
class TestMathFunctions(unittest.TestCase):
    """Tests for add() and divide()."""

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide_returns_float(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero_raises_error(self):
        # assertRaises passes only if the block raises the given exception
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_add_many_cases(self):
        # subTest runs every case and reports each failure separately,
        # instead of stopping at the first one.
        cases = [(1, 1, 2), (0, 0, 0), (-1, 1, 0), (2.5, 0.5, 3.0)]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)


#========================
# Part 1: Assertion Cheat Sheet
#========================
# self.assertEqual(a, b)              a == b
# self.assertNotEqual(a, b)           a != b
# self.assertTrue(x) / assertFalse(x) bool(x) is True / False
# self.assertIs(a, b)                 a is b (same object)
# self.assertIsNone(x)                x is None
# self.assertIn(item, container)      item in container
# self.assertAlmostEqual(a, b, places=2)   floats: 0.1 + 0.2 vs 0.3
# self.assertIsInstance(obj, cls)     isinstance(obj, cls)
# self.assertRaises(Error)            block must raise Error (use as a context manager)
#
# Test lifecycle (runs around EVERY test method):
#   setUp()     -> test_something() -> tearDown()
# setUpClass() / tearDownClass() run once per class (use for slow, shared setup).


#========================
# Part 2: Database Connection Basics (sqlite3)
#========================
# Python talks to databases through the DB-API standard. The steps are always:
#   1. connect()          open a connection
#   2. cursor()           get a cursor to run SQL
#   3. execute(sql, ...)  run a query
#   4. commit()           save changes (needed for INSERT / UPDATE / DELETE)
#   5. fetchone() / fetchall()  read results of a SELECT
#   6. close()            release the connection
#
# sqlite3 ships with Python and stores data in a single file. The special name
# ":memory:" creates a temporary database in RAM that disappears on close,
# which makes it perfect for demos and tests.
def demo_sqlite_basics():
    """Walk through the main sqlite3 operations and print the results."""
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # CREATE TABLE
    cursor.execute(
        """
        CREATE TABLE users (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
        """
    )

    # INSERT - ALWAYS pass values with "?" placeholders, never with f-strings.
    # Placeholders protect against SQL injection (see below).
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        ("Alice", "alice@example.com"),
    )
    # executemany(): the same statement for many rows
    cursor.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        [("Bob", "bob@example.com"), ("Carol", "carol@example.com")],
    )
    connection.commit()  # without commit() the changes are not saved

    # SELECT with fetchall() -> list of tuples
    cursor.execute("SELECT id, name, email FROM users")
    print(cursor.fetchall())
    # --> [(1, 'Alice', 'alice@example.com'), (2, 'Bob', 'bob@example.com'), (3, 'Carol', 'carol@example.com')]

    # SELECT with fetchone() -> a single tuple (or None when nothing matches)
    cursor.execute("SELECT name FROM users WHERE id = ?", (2,))
    print(cursor.fetchone())  # --> ('Bob',)

    cursor.execute("SELECT name FROM users WHERE id = ?", (99,))
    print(cursor.fetchone())  # --> None

    # row_factory = sqlite3.Row lets you read columns by NAME instead of position
    connection.row_factory = sqlite3.Row
    row = connection.execute("SELECT * FROM users WHERE id = ?", (1,)).fetchone()
    print(row["name"], dict(row))  # --> Alice {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}

    # SQL injection: why placeholders matter.
    # Building the query with an f-string lets the input rewrite the SQL itself.
    malicious_input = "x' OR '1'='1"
    unsafe_sql = f"SELECT name FROM users WHERE name = '{malicious_input}'"
    print(len(connection.execute(unsafe_sql).fetchall()))  # --> 3 (returned EVERY user!)

    safe_rows = connection.execute(
        "SELECT name FROM users WHERE name = ?", (malicious_input,)
    ).fetchall()
    print(len(safe_rows))  # --> 0 (the input is treated as plain text)

    # "with connection:" wraps a transaction: it commits if the block succeeds
    # and rolls back if an error is raised. (It does NOT close the connection.)
    try:
        with connection:
            connection.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                ("Dave", "dave@example.com"),
            )
            # Duplicate email violates the UNIQUE constraint -> IntegrityError
            connection.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                ("Eve", "alice@example.com"),
            )
    except sqlite3.IntegrityError as error:
        print(f"IntegrityError: {error}")  # --> IntegrityError: UNIQUE constraint failed: users.email

    # Dave was rolled back too, because both inserts belonged to one transaction
    print(connection.execute("SELECT COUNT(*) FROM users").fetchone()[0])  # --> 3

    connection.close()


#========================
# Part 3: Applying Both - A Repository Class
#========================
# A "repository" keeps all SQL for one table in one class. The connection is
# passed IN from outside (dependency injection), which is what makes the class
# easy to test: tests can hand it an in-memory database or a mock.
class UserRepository:
    """Create, read, update and delete rows of the users table."""

    def __init__(self, connection):
        self.connection = connection
        self.connection.row_factory = sqlite3.Row  # rows behave like dicts

    def create_table(self):
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id    INTEGER PRIMARY KEY AUTOINCREMENT,
                    name  TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
                """
            )

    def add_user(self, name, email):
        """Insert a user and return the new id."""
        if not name.strip():
            raise ValueError("Name cannot be empty")
        with self.connection:
            cursor = self.connection.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)", (name, email)
            )
        return cursor.lastrowid

    def get_user(self, user_id):
        """Return the user as a dict, or None if it does not exist."""
        row = self.connection.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return dict(row) if row else None

    def get_all_users(self):
        """Return every user as a list of dicts, ordered by id."""
        rows = self.connection.execute("SELECT * FROM users ORDER BY id").fetchall()
        return [dict(row) for row in rows]

    def update_email(self, user_id, new_email):
        """Change a user's email. Return True if a row was updated."""
        with self.connection:
            cursor = self.connection.execute(
                "UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)
            )
        return cursor.rowcount > 0

    def delete_user(self, user_id):
        """Delete a user. Return True if a row was deleted."""
        with self.connection:
            cursor = self.connection.execute(
                "DELETE FROM users WHERE id = ?", (user_id,)
            )
        return cursor.rowcount > 0


#========================
# Part 4: Testing Database Code (in-memory database)
#========================
# Golden rule: tests must NEVER touch your real database.
# Instead, setUp() builds a fresh ":memory:" database before every test and
# tearDown() closes it, so each test starts from a clean, known state.
class TestUserRepository(unittest.TestCase):
    """Tests for UserRepository against a real (but temporary) SQLite database."""

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.repo = UserRepository(self.connection)
        self.repo.create_table()

    def tearDown(self):
        self.connection.close()

    def test_add_user_returns_new_id(self):
        user_id = self.repo.add_user("Alice", "alice@example.com")
        self.assertEqual(user_id, 1)

    def test_get_user_returns_saved_data(self):
        user_id = self.repo.add_user("Alice", "alice@example.com")
        self.assertEqual(
            self.repo.get_user(user_id),
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
        )

    def test_get_missing_user_returns_none(self):
        self.assertIsNone(self.repo.get_user(999))

    def test_get_all_users_starts_empty(self):
        self.assertEqual(self.repo.get_all_users(), [])

    def test_get_all_users_returns_every_user_in_order(self):
        self.repo.add_user("Alice", "alice@example.com")
        self.repo.add_user("Bob", "bob@example.com")
        names = [user["name"] for user in self.repo.get_all_users()]
        self.assertEqual(names, ["Alice", "Bob"])

    def test_duplicate_email_raises_integrity_error(self):
        self.repo.add_user("Alice", "alice@example.com")
        with self.assertRaises(sqlite3.IntegrityError):
            self.repo.add_user("Impostor", "alice@example.com")

    def test_empty_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.repo.add_user("   ", "nobody@example.com")

    def test_update_email(self):
        user_id = self.repo.add_user("Alice", "old@example.com")
        self.assertTrue(self.repo.update_email(user_id, "new@example.com"))
        self.assertEqual(self.repo.get_user(user_id)["email"], "new@example.com")

    def test_update_missing_user_returns_false(self):
        self.assertFalse(self.repo.update_email(999, "x@example.com"))

    def test_delete_user(self):
        user_id = self.repo.add_user("Alice", "alice@example.com")
        self.assertTrue(self.repo.delete_user(user_id))
        self.assertIsNone(self.repo.get_user(user_id))


#========================
# Part 5: Testing Without a Database (unittest.mock)
#========================
# Sometimes the code under test only USES a repository or connection, and you
# want to test its own logic without any database at all. A mock is a fake
# object that records how it was called, so you can check those calls.
class UserService:
    """Business logic that depends on a repository (real or fake)."""

    def __init__(self, repository):
        self.repository = repository

    def register(self, name, email):
        user_id = self.repository.add_user(name, email)
        return f"Welcome {name}! Your id is {user_id}"


def open_database(path=":memory:"):
    """Open a SQLite connection with foreign-key checks switched on."""
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


class TestWithMocks(unittest.TestCase):
    """Tests that replace the database with mocks."""

    def test_register_builds_welcome_message(self):
        fake_repository = MagicMock()
        fake_repository.add_user.return_value = 7  # what the fake "returns"

        service = UserService(fake_repository)
        message = service.register("Alice", "alice@example.com")

        self.assertEqual(message, "Welcome Alice! Your id is 7")
        # Verify the service called the repository exactly as expected
        fake_repository.add_user.assert_called_once_with("Alice", "alice@example.com")

    # patch() temporarily replaces sqlite3.connect, so no file is ever opened.
    # The mock is passed to the test as an extra argument.
    @patch("sqlite3.connect")
    def test_open_database_enables_foreign_keys(self, mock_connect):
        connection = open_database("app.db")

        mock_connect.assert_called_once_with("app.db")
        connection.execute.assert_called_once_with("PRAGMA foreign_keys = ON")


#========================
# Part 6: Running the Tests
#========================
# From a terminal (the file name must be importable, so avoid leading digits
# if you use the module form; the direct form below always works):
#   python 08_unit_testing_and_databases.py              run this file
#   python -m unittest -v                                discover and run all test_*.py files
#   python -m unittest test_users.TestUserRepository     run one class
#   python -m unittest test_users.TestUserRepository.test_delete_user   run one test
#
# Reading the results:
#   .  test passed      F  test failed (an assertion was wrong)      E  test raised an error
#
# Project layout used in real projects:
#   my_project/
#       users.py            <- the code (UserRepository, ...)
#       test_users.py       <- the tests (import from users)


#========================
# Part 6: Applying This to MySQL / PostgreSQL
#========================
# Only the connection step changes. The cursor / execute / fetch / commit /
# close workflow is the same DB-API pattern, and the placeholder becomes %s.
#
#   MySQL       pip install mysql-connector-python
#       import mysql.connector
#       connection = mysql.connector.connect(
#           host="localhost", user="root", password="...", database="sakila")
#       cursor = connection.cursor()
#       cursor.execute("SELECT * FROM actor WHERE actor_id = %s", (1,))
#
#   PostgreSQL  pip install psycopg2-binary
#       import psycopg2
#       connection = psycopg2.connect(
#           host="localhost", dbname="mydb", user="postgres", password="...")
#
# How to test code that uses them:
#   - Because the connection is injected (see UserRepository), tests can pass a
#     SQLite ":memory:" connection or a MagicMock instead of the real server.
#   - Keep credentials out of the code (environment variables, never commit them).
#   - If the SQL differs between engines (e.g. "?" vs "%s"), test the real
#     engine separately in an integration test against a dedicated test database.
#   - pytest is a popular alternative: plain functions named test_*, plain
#     `assert` statements and fixtures instead of setUp / tearDown.


#========================
# Main: Run the Demo and the Tests
#========================
if __name__ == "__main__":
    print("--- sqlite3 demo ---")
    demo_sqlite_basics()

    print("\n--- running unit tests ---")
    unittest.main(verbosity=2)  # verbosity=2 prints the name of every test