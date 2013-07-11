
#
# * GET home page.
#
exports.index = (req, res) ->
	res.render "index",
		title: "Express"

	db = new exports.sqlite3.Database("../sqlite3")
	db.serialize ->
		db.all "SELECT * from latitude", (err, rows) ->
			console.log rows if !err