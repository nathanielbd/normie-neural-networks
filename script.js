/*
generate data-m111111-ignore-stats.csv
*/

var values = []
for (var i = 1; i < 36; i++) {
    var to_select = document.querySelectorAll(`.question > input[name='q${i}']`)[Math.floor(Math.random()*document.querySelectorAll(`.question > input[name='q${i}']`).length)]
    to_select.click()
    values.push(to_select.value)
}

// the call here to `.click()` does not work -- thus all the data corresponds
// to answering the default answers to the stats questions -- male, Below 150cm (Below 4'10"), Below 3, etc.
// and we should ignore the answers to the stats questions
for (var j = 36; j < 42; j++) {
    var to_select = document.querySelectorAll(`#q${j} > option`)[Math.floor(Math.random()*document.querySelectorAll(`#q${j} > option`).length)]
    to_select.click()
    values.push(to_select.value)
}

// this would be the correct way of generating data with random answers to the stats questions:
// for (var j = 36; j < 42; j++) {
//     $(`#q${j}`).selectedIndex = Math.floor(Math.random()*document.querySelectorAll(`#q${j} > option`).length)
//     var to_select = document.querySelectorAll(`#q${j} > option`)[$(`#q${j}`).selectedIndex]
//     values.push(to_select.value)
// }

// we're not answering honestly
$('#honest').selectedIndex = 1
// fill out Robot test first
console.log(values.toString())