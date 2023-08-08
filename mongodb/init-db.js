
// Load env vars
const MONGO_DB_USERNAME = process.env.MONGO_DB_USERNAME
const MONGO_DB_PASSWORD = process.env.MONGO_DB_PASSWORD
const MONGO_INITDB_DATABASE = process.env.MONGO_INITDB_DATABASE

// const sampleScrapData = require("/sample-data/users-scrapdata.json")

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

// create collections
// db.createCollection("users")
// db.createCollection("userExternalCredentials")
// db.createCollection("messages")
// db.createCollection("scrapData")
// db.createCollection("scrapTasks")

// // Create indexes
// db.users.createIndex({ username: 1 })
// db.userExternalCredentials.createIndex({ userId: 1 })
// db.userExternalCredentials.createIndex({ userId: 1, externalPlatformId: 1 })
// db.messages.createIndex({ userId: 1 })
// db.messages.createIndex({ username: 1 })
// db.scrapData.createIndex({ userId: 1 })
// db.scrapData.createIndex({ taskId: 1 })
// db.scrapTasks.createIndex({ userId: 1 })
// db.scrapTasks.createIndex({ taskId: 1 })
// db.scrapTasks.createIndex({ status: 1 })
// db.scrapTasks.createIndex({ userId: 1, status: 1 })

// sampleUsers.forEach(user => {
//     let userToInsert = user
//     userToInsert.addedDateTime = new Date(userToInsert.addedDateTime)
//     db.users.insertOne(user)
// })

// const users = db.users.find({}).toArray()

// sampleMessages.forEach(message => {
//     let messageToInsert = message
//     let userMatch = users.find(user => user.username === message.username)
//     if (userMatch) {
//         messageToInsert.userId = userMatch._id.toString()
//         messageToInsert.addedDateTime = new Date(messageToInsert.addedDateTime)
//         delete messageToInsert.username
//         db.messages.insertOne(messageToInsert)
//     }
// })

// sampleExternalCredentials.forEach(externalCredential => {
//     let externalCredentialToInsert = externalCredential
//     externalCredentialToInsert.userId = users.find(user => user.username === externalCredential.username)._id.toString()
//     delete externalCredentialToInsert.username
//     db.userExternalCredentials.insertOne(externalCredentialToInsert)
// })

// sampleScrapTasks.forEach(scrapTask => {
//     let scrapTaskToInsert = scrapTask
//     scrapTaskToInsert.userId = users.find(user => user.username === scrapTask.username)._id.toString()
//     scrapTaskToInsert.addedDateTime = new Date(scrapTaskToInsert.addedDateTime)
//     delete scrapTaskToInsert.username
//     db.scrapTasks.insertOne(scrapTaskToInsert)
// })

