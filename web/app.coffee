
###
Module dependencies.
###
express = require("express")
routes = require("./routes")
http = require("http")
path = require("path")
app = express()
sqlite3 = require("sqlite3").verbose()


# all environments
app.set "port", process.env.PORT or 3000
app.set "views", __dirname + "/views"
app.set "view engine", "jade"
app.use express.favicon()
app.use express.logger("dev")
app.use express.bodyParser()
app.use express.methodOverride()
app.use app.router
app.use require("stylus").middleware(__dirname + "/public")
app.use express.static(path.join(__dirname, "public"))

# development only
app.use express.errorHandler()  if "development" is app.get("env")
app.get "/", (req, res)->
  db = new sqlite3.Database("../sqlite3")
  db.serialize ->
    db.all "SELECT * FROM latitude ORDER BY time DESC LIMIT 20", (err, rows) ->
      res.render "index",
        title: "hayatitude"
        latitudes: rows if !err


http.createServer(app).listen app.get("port"), ->
  console.log "Express server listening on port " + app.get("port")

