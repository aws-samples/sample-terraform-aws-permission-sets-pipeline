# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

output "permission_sets" {
  value = try({ for k, v in module.aws_permission_sets.permission_sets : k => v.arn }, null)
}

output "assignments" {
  value = try({ for v in module.aws_permission_sets.assignments : v.permission_set_arn => v.id... }, null)
}
