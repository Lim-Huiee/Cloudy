import AWS from 'aws-sdk';

AWS.config.update({
  accessKeyId: 'AKIAUU3QCWRZY4745T62',      // Replace with your Access Key ID
  secretAccessKey: 'l6iCK1kYwGmViPkSKcclrfr6TkJuy2gG0XIHof5Z',  // Replace with your Secret Access Key
  region: 'ap-southeast-1',                    // Replace with your desired AWS region
});

export default AWS;
