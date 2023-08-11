
// Load env vars
const MONGO_DB_USERNAME = process.env.MONGO_DB_USERNAME
const MONGO_DB_PASSWORD = process.env.MONGO_DB_PASSWORD
const MONGO_INITDB_DATABASE = process.env.MONGO_INITDB_DATABASE

// Create default user to login in app database
db = db.getSiblingDB('admin');
db.createUser({
    user: MONGO_DB_USERNAME,
    pwd: MONGO_DB_PASSWORD,
    roles: [
        { role: "readWrite", db: MONGO_INITDB_DATABASE }
    ]
});

db = db.getSiblingDB(MONGO_INITDB_DATABASE);