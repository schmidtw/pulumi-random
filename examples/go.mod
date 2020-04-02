module github.com/pulumi/pulumi-random/examples

go 1.13

require github.com/pulumi/pulumi/pkg v1.13.1

replace (
	github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
	github.com/pulumi/pulumi-random/sdk => ../sdk
)