import { getDB, saveDB, initDB } from './init'

export async function createReport(component_id, message, browser_data) {
  await initDB()
  const db = getDB()
  const created_at = new Date().toISOString()
  try {
    db.run('INSERT INTO reports (component_id, message, browser_data, created_at) VALUES (?, ?, ?, ?)', [component_id, message, browser_data, created_at])
    await saveDB()
    return true
  } catch (err) {
    throw err
  }
}

export async function getReports() {
  await initDB()
  const db = getDB()
  const res = db.exec('SELECT id, component_id, message, browser_data, created_at FROM reports ORDER BY id DESC')
  if (!res || !res.length) return []
  const cols = res[0].columns
  const values = res[0].values
  return values.map(row => {
    const obj = {}
    cols.forEach((c, i) => (obj[c] = row[i]))
    return obj
  })
}

export default { createReport, getReports }
