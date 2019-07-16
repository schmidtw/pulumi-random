module github.com/pulumi/pulumi-random

go 1.12

require (
	github.com/hashicorp/terraform v0.12.0-rc1.0.20190509225429-28b2383eacae
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v0.17.23-0.20190715212628-02ffff88409f
	github.com/pulumi/pulumi-terraform v0.18.4-0.20190716205920-bd76158611ad
	github.com/stretchr/testify v1.3.1-0.20190311161405-34c6fa2dc709
	github.com/terraform-providers/terraform-provider-random v0.0.0-20190430215304-58e0a7183d4f
	labix.org/v2/mgo v0.0.0-20140701140051-000000000287 // indirect
	launchpad.net/gocheck v0.0.0-20140225173054-000000000087 // indirect
)

replace (
	github.com/Nvveen/Gotty => github.com/ijc25/Gotty v0.0.0-20170406111628-a8b993ba6abd
	github.com/golang/glog => github.com/pulumi/glog v0.0.0-20180820174630-7eaa6ffb71e4
)
