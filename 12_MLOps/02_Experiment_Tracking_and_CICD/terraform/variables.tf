variable "aws_region" {
  description = "AWS region for provisioning MLOps infrastructure"
  type        = str
  default     = "us-east-1"
}

variable "project_name" {
  description = "Identifier for the MLOps project"
  type        = str
  default     = "ride-duration-mlops"
}

variable "environment" {
  description = "Deployment environment stage (dev, staging, prod)"
  type        = str
  default     = "prod"
}
