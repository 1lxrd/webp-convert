dir = '/home/xnelxrd/Documents/'; //variable with path to files

//!!! BEFORE USING CREATE RESULT FOLDER in this directory !!!

temp = /(.+\.jpg)|(.+\.jpeg)|(.+\.png)/ //regular for checking if filetype is image, add more if u want to use another type of image

const webp=require('webp-converter');
const fs = require('fs');
fs.readdir(dir,(err, files) => { //opening folder with files
    if (err) throw err;

    for (i in files){ //cycle for finding all files
        let a = temp.test(files[i]); //checking if filetype is an image (comparing to regular expression)
        if (a){
            namef = files[i].split('.'); //receiving name of image, DON'T USE DOT IN FILENAMES
            const result = webp.cwebp(files[i],`result/${namef[0]}.webp`,"-q 80",logging="-v"); //converting
            result.then((response) => {
            console.log(response); //logging
            });
        }
    }

})
