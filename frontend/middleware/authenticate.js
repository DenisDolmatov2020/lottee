export default function ({ store, redirect }) {
  if (!store.getters['user/isAuthenticated']) {
    redirect('/login?message=login')
  }
}
