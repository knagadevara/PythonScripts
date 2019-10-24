provider "aws" {
    access_key =    "AKIAJBQNQKK2NG4HBIJQ"
    secret_key =    "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"
    region =    "ap-south-1"  
}

resource "aws_s3_bucket" "knagadevara_s3_bucket" {
    bucket = "knagadevara_s3_bucket"
    region = "ap-south-1"
    
}

