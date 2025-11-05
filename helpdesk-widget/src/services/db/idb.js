const DB_STORE_NAME = 'helpdesk-db-store'

export function openIDB() {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open(DB_STORE_NAME, 1)
    req.onupgradeneeded = e => {
      const idb = e.target.result
      if (!idb.objectStoreNames.contains('files')) idb.createObjectStore('files')
    }
    req.onsuccess = e => resolve(e.target.result)
    req.onerror = e => reject(e.target.error)
  })
}

export function idbGet(key) {
  return new Promise(async (resolve, reject) => {
    try {
      const idb = await openIDB()
      const tx = idb.transaction('files', 'readonly')
      const store = tx.objectStore('files')
      const req = store.get(key)
      req.onsuccess = e => {
        resolve(e.target.result || null)
        idb.close()
      }
      req.onerror = e => {
        idb.close()
        reject(e.target.error)
      }
    } catch (err) {
      reject(err)
    }
  })
}

export function idbSet(key, value) {
  return new Promise(async (resolve, reject) => {
    try {
      const idb = await openIDB()
      const tx = idb.transaction('files', 'readwrite')
      const store = tx.objectStore('files')
      const req = store.put(value, key)
      req.onsuccess = () => {
        resolve()
        idb.close()
      }
      req.onerror = e => {
        idb.close()
        reject(e.target.error)
      }
    } catch (err) {
      reject(err)
    }
  })
}

export default { openIDB, idbGet, idbSet }
