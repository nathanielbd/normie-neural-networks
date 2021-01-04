/*
generate data.csv
*/

var values = []
for (var i = 1; i < 36; i++) {
    var to_select = document.querySelectorAll(`.question > input[name='q${i}']`)[Math.floor(Math.random()*document.querySelectorAll(`.question > input[name='q${i}']`).length)]
    to_select.click()
    values.push(to_select.value)
}
for (var j = 36; j < 42; j++) {
    $(`#q${j}`).selectedIndex = Math.floor(Math.random()*document.querySelectorAll(`#q${j} > option`).length)
    var to_select = document.querySelectorAll(`#q${j} > option`)[$(`#q${j}`).selectedIndex]
    values.push(to_select.value)
}
// we're not answering honestly
$('#honest').selectedIndex = 1
// fill out Robot test first
console.log(values.toString())

/*
generate data-with-stats.csv
*/

var values = []
for (var i = 1; i < 36; i++) {
    var to_select = document.querySelectorAll(`.question > input[name='q${i}']`)[Math.floor(Math.random()*document.querySelectorAll(`.question > input[name='q${i}']`).length)]
    to_select.click()
    values.push(to_select.value)
}
for (var j = 36; j < 42; j++) {
    var to_select = document.querySelectorAll(`#q${j} > option`)[Math.floor(Math.random()*document.querySelectorAll(`#q${j} > option`).length)]
    to_select.click()
    values.push(to_select.value)
}
// we're not answering honestly
$('#honest').selectedIndex = 1
// fill out Robot test first
console.log(values.toString())

/*
generate data-with-outliers.csv
*/

const x_outliers = [
    // very negative X
    'YNNYNNNYN',
    // very positive X
    'NYYNYYYNY'
]

const y_outliers = [
    // very negative Y
    'DDDADDNNADNDDNANNNAA-DDDDD',
    // very positive Y
    'AAADAAYYDAYAAYDYYYDD-AAAAA'
]

const stats_combs = [
    // ['othersex', 'male', 'female'],
    // ['11', '12', '13', '14', '15'],
    // ['21', '22', '23', '24'],
    // ['31', '32', '33', '34'],
    // ['41', '42', '43'],
    // ['51', '52', '53', '54']
    [0, 1, 2],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 1, 2],
    [0, 1, 2, 3]
]

var rand_xy_seq = y_outliers[Math.floor(Math.random()*2)].replace('-', x_outliers[Math.floor(Math.random()*2)])
var rand_values = [...rand_xy_seq]
for (const ls in stats_combs) {
    var sub_ls = stats_combs[ls]
    rand_values.push(sub_ls[Math.floor(Math.random()*sub_ls.length)])
}

for (var i = 1; i < 36; i++) {
    var to_select = document.querySelector(`.question > input[name='q${i}'][value='${rand_values[i-1]}']`)
    to_select.click()
}
for (var j = 36; j < 42; j++) {
    var to_select = document.querySelector(`#q${j} > option[value='${rand_values[j-1]}']`)
    to_select.click()
}
// we're not answering honestly
$('#honest').selectedIndex = 1
// fill out Robot test first
console.log(rand_values.toString())