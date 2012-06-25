/**
* @author Pierre-Henry Soria <pierrehs@hotmail.com>
* @link http://github.com/pH-7
* @copyright Copyright pH7 Script All Rights Reserved.
* @license CC-BY - http://creativecommons.org/licenses/by/3.0/
*/

var sFolder = sUrl + 'static/js/';
var aFileList = [
    'lib/tipsy',
    'common'
];

for(i in aFileList)
    document.write('<script src="' + sFolder + aFileList[i] + '.js"></script>\n');
