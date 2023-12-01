// Solved in REPL, did this afterhand
const { readFileSync } = require('node:fs');
const a = readFileSync('input.txt').toString().split`\n`.filter(x => x);
let s = 0;

// Part 1
a.map(v => v.split``.filter(e => /\d/.test(e)).join``).map(v => s = s + +(v[0]+v.at(-1)));
console.log('Part 1', s);

// Part 2
const nums=['öööö', "one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","twentyone","twentytwo","twentythree","twentyfour","twentyfive","twentysix","twentyseven","twentyeight","twentynine","thirty","thirtyone","thirtytwo","thirtythree","thirtyfour","thirtyfive","thirtysix","thirtyseven","thirtyeight","thirtynine","forty","fortyone","fortytwo","fortythree","fortyfour","fortyfive","fortysix","fortyseven","fortyeight","fortynine","fifty","fiftyone","fiftytwo","fiftythree","fiftyfour","fiftyfive","fiftysix","fiftyseven","fiftyeight","fiftynine","sixty","sixtyone","sixtytwo","sixtythree","sixtyfour","sixtyfive","sixtysix","sixtyseven","sixtyeight","sixtynine","seventy","seventyone","seventytwo","seventythree","seventyfour","seventyfive","seventysix","seventyseven","seventyeight","seventynine","eighty","eightyone","eightytwo","eightythree","eightyfour","eightyfive","eightysix","eightyseven","eightyeight","eightynine","ninety","ninetyone","ninetytwo","ninetythree","ninetyfour","ninetyfive","ninetysix","ninetyseven","ninetyeight","ninetynine"];
s = 0;
for(v of a) { for(var i = nums.length - 1; i > 0; --i) v=v.replaceAll(nums[i],`${nums[i][0]}${i}${nums[i].at(-1)}`); v=v.split``.filter(x=>/\d/.test(x)).join``; /*console.log(v);*/s+= +(v[0]+v.at(-1))}
console.log('Part 2', s);
