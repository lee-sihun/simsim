const mariadb = require("mariadb");
const pool = mariadb.createPool({
  host: "127.0.0.1",
  port: 3306, // default: 3306
  database: "simsim",
  user: "root",
  password: "0000",
});

async function search_data(pool) {
  let conn;
  try {
    conn = await pool.getConnection();

    const rows = await conn.query("SELECT qs,ans FROM Text");
    return rows;
  } catch (err) {
    throw err;
  } finally {
    if (conn) conn.release(); // release pool
  }
}

function ext_data(data) {
  var qs = [];
  var ans = [];
  for (i = 0; i <= data.length; i++) {
    if (data[i] == undefined) {
      break;
    }
    qs.push(data[i]["qs"]);
    ans.push(data[i]["ans"]);
  }

  var qsData = JSON.stringify(qs);
  var ansData = JSON.stringify(ans);

  var fs = require("fs");
  fs.writeFile("qs.txt", qsData, function (err) {
    if (err) {
      console.log(err);
    }
  });

  fs.writeFile("ans.txt", ansData, function (err) {
    if (err) {
      console.log(err);
    }
  });
}

search_data(pool).then((response) => ext_data(response)); // 원하는 값인 data를 출력할 수 있습니다
