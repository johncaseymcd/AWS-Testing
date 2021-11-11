const aws = require("aws-sdk");
const s3 = new aws.S3();

exports.handler = async(event, context) => {
    var destinationBucket = "nps26-new-receiver";
    var params = {
        CopySource: event.Records[0].s3.bucket.name,
        Key: event.Records[0].s3.object.key,
        Bucket: destinationBucket
    }
    
    s3.copyObject(params, function(err, data){
        if (err){
            console.log(err, err.stack);
        }
        else{
            console.log(data);
        }
    });
    
    return {
        statusCode: 200,
        body: JSON.stringify("Hello from the File Mover function!")
    };
}