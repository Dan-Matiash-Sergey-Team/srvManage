async function main(str) {
    const MongoClient = require('mongodb').MongoClient
    const mongoUrl = 'mongodb://universai:cumzone@127.0.0.1:1488'
    const client = await new MongoClient(mongoUrl);
    await client.connect()
    const db = await client.db('dtpsFull');

    y = req.query.id.slice(0, 4)
    m = req.query.id.slice(4, 6)

    let dtpsList = await db.collection(`${y}${m}`).find({"id" : req.query.id}).toArray()
    return dtpsList
}

main('20170613').then((res) => console.log(res))