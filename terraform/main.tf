
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "emotion_recognition_logs" {
  bucket = "emotion-recognition-logs-bucket"
  acl    = "private"
}
