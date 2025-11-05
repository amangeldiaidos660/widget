
import init from './db/init'
import * as users from './db/users'
import * as comps from './db/components'
import * as reports from './db/reports'

export const initDB = init.initDB
export const getDB = init.getDB
export const saveDB = init.saveDB
export const createUser = users.createUser
export const getUserByUsername = users.getUserByUsername
export const verifyUser = users.verifyUser
export const hashPassword = users.hashPassword
export const createComponent = comps.createComponent
export const getComponentsByUser = comps.getComponentsByUser
export const createReport = reports.createReport
export const getReports = reports.getReports

export default {
  initDB,
  getDB,
  saveDB,
  createUser,
  getUserByUsername,
  verifyUser,
  hashPassword,
  createComponent,
  getComponentsByUser,
  createReport,
  getReports,
}

