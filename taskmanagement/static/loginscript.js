function togglePass(id, btn) {
  const input = document.getElementById(id)
  if (!input) return

  const isPassword = input.type === 'password'
  input.type = isPassword ? 'text' : 'password'
  btn.textContent = isPassword ? 'Hide' : 'Show'
}