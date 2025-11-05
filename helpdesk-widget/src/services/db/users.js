import { getDB, saveDB, initDB } from './init'

function rowToObj(res) {
  if (!res || !res.length) return null
  const cols = res[0].columns
  const row = res[0].values[0]
  const obj = {}
  cols.forEach((c, i) => (obj[c] = row[i]))
  return obj
}

export async function createUser(username, passwordHash) {
  await initDB()
  const db = getDB()
  try {
    db.run('INSERT INTO users (username, password) VALUES (?, ?)', [username, passwordHash])
    await saveDB()
    return true
  } catch (err) {
    throw err
  }
}

export async function getUserByUsername(username) {
  await initDB()
  const db = getDB()
  const safe = String(username).replace(/'/g, "''")
  const res = db.exec(`SELECT id, username, password FROM users WHERE username = '${safe}' LIMIT 1`)
  return rowToObj(res)
}

export async function verifyUser(username, passwordHash) {
  const user = await getUserByUsername(username)
  if (!user) return false
  return user.password === passwordHash
}

export async function hashPassword(plain) {
  const enc = new TextEncoder().encode(plain)
  const hashBuffer = await crypto.subtle.digest('SHA-256', enc)
  const hashArray = Array.from(new Uint8Array(hashBuffer))
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('')
  return hashHex
}

export default { createUser, getUserByUsername, verifyUser, hashPassword }
