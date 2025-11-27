import { API_ENDPOINTS } from './backendEndpoints.js'

export async function fetchHealth() {
  const res = await fetch(API_ENDPOINTS.health);
  if (!res.ok) throw new Error('API error');
  return await res.json();
}
