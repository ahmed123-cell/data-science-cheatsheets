# ==============================================================================
# Terraform Infrastructure as Code (IaC) for MLOps Artifact Storage
# Provisions:
# 1. AWS S3 Bucket for DVC remote data and MLflow model artifacts
# 2. S3 Bucket Versioning (essential for artifact immutability)
# 3. Server-Side Encryption (AES256)
# 4. AWS DynamoDB Table for Terraform distributed state locking
# ==============================================================================

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# S3 Bucket for DVC and MLflow Artifacts
resource "aws_s3_bucket" "mlops_artifacts" {
  bucket        = "${var.project_name}-${var.environment}-artifacts-${var.aws_region}"
  force_destroy = false

  tags = {
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "Terraform"
  }
}

# Enable Object Versioning for Model & Data Auditability
resource "aws_s3_bucket_versioning" "artifacts_versioning" {
  bucket = aws_s3_bucket.mlops_artifacts.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Server-Side Encryption Configuration
resource "aws_s3_bucket_server_side_encryption_configuration" "artifacts_encryption" {
  bucket = aws_s3_bucket.mlops_artifacts.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Block Public Access (Security Compliance)
resource "aws_s3_bucket_public_access_block" "artifacts_public_block" {
  bucket = aws_s3_bucket.mlops_artifacts.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# DynamoDB Table for Terraform State Locking
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "${var.project_name}-terraform-state-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "Terraform"
  }
}
