# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

module "aws_permission_sets" {
  #checkov:skip=CKV_TF_1,CKV_TF_2: This is a sample, and should use the latest module version
  source = "aws-ia/permission-sets/aws"

  templates_path = "./templates"
  tags = {
    "managed-by" = "aws-ps-pipeline"
  }
}
