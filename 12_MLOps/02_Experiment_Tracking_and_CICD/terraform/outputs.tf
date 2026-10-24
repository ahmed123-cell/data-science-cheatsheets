output "s3_bucket_name" {
  description = "Name of the created S3 artifact bucket"
  value       = aws_s3_bucket.mlops_artifacts.id
}

output "s3_bucket_arn" {
  description = "ARN of the S3 artifact bucket"
  value       = aws_s3_bucket.mlops_artifacts.arn
}

output "dynamodb_lock_table_name" {
  description = "Name of the DynamoDB table used for Terraform state locking"
  value       = aws_dynamodb_table.terraform_locks.name
}
