import initSqlJs from 'sql.js'
import wasmUrl from 'sql.js/dist/sql-wasm.wasm?url'
import { idbGet, idbSet } from './idb'

let SQL = null
let db = null
const DB_KEY = 'helpdesk_sqlite_file_v1'

export async function initDB() {
  if (db) return db
  SQL = await initSqlJs({ locateFile: () => wasmUrl })
  const saved = await idbGet(DB_KEY)
  if (saved) {
    db = new SQL.Database(new Uint8Array(saved))
  } else {
    db = new SQL.Database()
  }
  await ensureSchema()
  await saveDB()
  if (typeof window !== 'undefined') window.__helpdesk_db = db
  return db
}

export function getDB() {
  if (!db) throw new Error('DB not initialized')
  return db
}

export async function saveDB() {
  if (!db) throw new Error('DB not initialized')
  const data = db.export()
  await idbSet(DB_KEY, data.buffer)
}

async function ensureSchema() {
  const schema = `
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE,
      password TEXT
    );

    CREATE TABLE IF NOT EXISTS components (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER,
      name TEXT,
      script_code TEXT,
      created_at TEXT
    );

    CREATE TABLE IF NOT EXISTS reports (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      component_id INTEGER,
      message TEXT,
      browser_data TEXT,
      created_at TEXT
    );
  `
  db.exec(schema)
}

export default { initDB, getDB, saveDB }
