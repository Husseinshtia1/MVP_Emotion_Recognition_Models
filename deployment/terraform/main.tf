
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "emotion_recognition" {
  bucket = "emotion-recognition-logs-bucket"
  acl    = "private"
}
