const toBytes = (text) => {
  const surrogate = encodeURIComponent(text);
  const result = [];
  for (let i = 0; i < surrogate.length; ) {
    const character = surrogate[i];
    i += 1;
    if (character == "%") {
      const hex = surrogate.substring(i, (i += 2));
      if (hex) {
        result.push(parseInt(hex, 16));
      }
    } else {
      result.push(character.charCodeAt(0));
    }
  }
  return result;
};

const similarity_check = (answer, input) => {
  var difflib = require("difflib");
  var answer_bytes = toBytes(answer);
  var input_bytes = toBytes(input);
  var similarity = new difflib.SequenceMatcher(null, answer_bytes, input_bytes);
  return similarity.ratio();
};

// var a = "안녕";
// var b = "안녕?";
// console.log(similarity_check(a, b));
