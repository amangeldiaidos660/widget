import { getDB, saveDB, initDB } from './init'

function rowsToArray(res) {
  if (!res || !res.length) return []
  const cols = res[0].columns
  const values = res[0].values
  return values.map(row => {
    const obj = {}
    cols.forEach((c, i) => (obj[c] = row[i]))
    return obj
  })
}

export async function createComponent(user_id, name) {
  await initDB()
  const db = getDB()
  const created_at = new Date().toISOString()
  try {
    db.run('INSERT INTO components (user_id, name, script_code, created_at) VALUES (?, ?, ?, ?)', [user_id, name, null, created_at])
    const res = db.exec('SELECT last_insert_rowid() AS id')
    let id = null
    if (res && res[0] && res[0].values && res[0].values[0]) {
      id = res[0].values[0][0]
    }
    const script_code = `<script src="widget.js" data-id="${id}"></script>`
    db.run('UPDATE components SET script_code = ? WHERE id = ?', [script_code, id])
    await saveDB()
    return { id, user_id, name, script_code, created_at }
  } catch (err) {
    throw err
  }
}

export async function getComponentsByUser(user_id) {
  await initDB()
  const db = getDB()
  const uid = Number(user_id) || 0
  const res = db.exec(`SELECT id, user_id, name, script_code, created_at FROM components WHERE user_id = ${uid} ORDER BY id DESC`)
  return rowsToArray(res)
}

export default { createComponent, getComponentsByUser }
