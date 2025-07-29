# AWS Permission Set Pipeline

This solution enables you to dynamically manage [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) Permission Sets through infrastructure as code using a CI/CD pipeline built with native AWS services. Furthermore, it enables a seamless integration of the Permission Set assignment mechanism with the [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) lifecycle events or [Account Factory for Terraform](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) (AFT) environment, providing dynamic identity configurations for both new and existing AWS accounts.

The solution implements Amazon EventBridge rules to monitor AWS account creation and update, ensuring your identity configurations remain synchronized with your organizational structure. After creating/updating accounts in Control Tower or AFT, the pipeline will be triggered to evaluate a set of JSON files with Permission Set definitions and assignment rules, to then apply and synchronize the settings across all accounts.

The main Terraform code relies on the oficial AWS [permission-sets](https://registry.terraform.io/modules/aws-ia/permission-sets/aws/latest) Terraform module, that can dynamically create, update, delete and assign Permission Sets in Identity Center, based on the JSON files.

## Table of Contents

- [Diagram](#diagram)
- [Prerequisites](#prerequisites)
- [Limitations](#limitations)
- [Versions](#versions)
- [Security](#security)
- [License](#license)

## Diagram

![diagram](assets/diagram/aws-ps-pipeline.jpg)

---

## Prerequisites

- A multi-account environment with AWS Control Tower and AWS Organizations already set up.
- Optionally you can use AFT in conjunction with AWS Control Tower.
- Prepare the VCS repo that will handle the main code. You can see a sample in the solution [repository](https://github.com/aws-samples/sample-terraform-aws-permission-sets-pipeline/tree/main/samples/basic).
- Prepare an IAM Identity Center delegated administrator AWS account to receive the solution. See more in [AWS IAM Identity Center delegated administration](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html).

## Limitations

The pipeline uses AWS native resources and Terraform Open-Source version, it's not prepared to make calls to third-party ecosystems, such as Terraform Cloud.

## Versions

- Terraform: >=1.6

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.