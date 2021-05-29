const MongoClient = require('mongodb').MongoClient
const fs = require('fs')

function parse(data) {
	let res = {
		"NPDD": []
	}
	res['id'] = data['id']
	res['year'] = data['year']
	res['month'] = data['month']
	res['date'] = data['data']['date']
	res['DTP_V'] = data['data']['DTP_V']
	res['osv'] = data['data']['infoDtp']['osv']
	res['OBJ_DTP'] = data['data']['infoDtp']['OBJ_DTP']
	res['COORD_W'] = data['data']['infoDtp']['COORD_W']
	res['COORD_L'] = data['data']['infoDtp']['COORD_L']

	let add = ""
	let s = data['data']['infoDtp']['street']
	let h = data['data']['infoDtp']['house'].replace(' ', '/')
	let d = data['data']['infoDtp']['dor']
	let km = data['data']['infoDtp']['km']
	let m = data['data']['infoDtp']['m']
	res['street'] = s
	res['district'] = data['district_name']
	if (km != "" && d != "") {
		add = d + ", " + km + "км" + (m != "0" ? ", " + m + "м" : "")
	} else if (s != "") {
		add = s + ", д " + h
	} else {
		add = "Точный адрес происшествия не указан"
	}
	res['address'] = add

	for (let ts of data['data']['infoDtp']['ts_info']) {
		for (let uc of ts['ts_uch']) {
			if (!uc['NPDD'].includes('Нет нарушений')) {
				for (let n of uc['NPDD']) {
					if (!res['NPDD'].includes(n)) res['NPDD'].push(n)
				}
			}
		}
	}

	for (let uc of data['data']['infoDtp']['uchInfo']) {
		if (!uc['NPDD'].includes('Нет нарушений')) {
			for (let n of uc['NPDD']) {
				if (!res['NPDD'].includes(n)) res['NPDD'].push(n)
			}
		}

	}

	let dcount = 0
	for (let ts of data['data']['infoDtp']['ts_info']) {
		for (let tsuc of ts['ts_uch']) {
			if (tsuc['S_T'].toLowerCase().includes('скончался')) dcount++
		}
	}
	for (let uc of data['data']['infoDtp']['uchInfo']) {
		if (uc['S_T'].toLowerCase().includes('скончался')) dcount++
	}
	res['death'] = dcount

	return res
}

async function main() {
	const mongoUrl = 'mongodb://universai:cumzone@127.0.0.1:1488'
	const client = await new MongoClient(mongoUrl);
	await client.connect()
	const db1 = await client.db('dtpsLite');
	const db2 = await client.db('dtpsFull');

	for (let y = 2015; y < 2022; y++) {
		for (let m = 1; m < 13; m++) {
			console.log(y + ":" + m)
			let month = m < 10 ? `0${m}`: m
			let collectionI = db2.collection(`${y}${month}`)
			const collection = db1.collection(`${y}${month}`)
			for (let el of (await collectionI.find({}).toArray())) {
				collection.insertOne(parse(el))
			}
		}
	}
	console.log("Finish")
}

main().then(function () {})
