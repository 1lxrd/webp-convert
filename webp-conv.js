dir = './'; //variable with path to files

temp = /(.+\.jpg)|(.+\.jpeg)|(.+\.png)|(.+\.JPG)|(.+\.JPEG)/ //regular for checking if filetype is image, add more if u want to use another type of image

const webp=require('webp-converter');
const fs = require('fs');

fs.readdir(dir,(err, files) => { //opening folder with files
    if (err) throw err;

    for (i in files){ //cycle for finding all files
        let a = temp.test(files[i]); //checking if filetype is an image (comparing to regular expression)
        if (a){
            const result = webp.cwebp(files[i],files[i],'-q 70',logging="-v"); //converting
            result.then((response) => {
            console.log(response); //logging
            });

        }
    }

})
