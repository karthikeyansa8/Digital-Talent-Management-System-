function togglePass(id, btn) {
  const input = document.getElementById(id)
  if (!input) return

  const isPassword = input.type === 'password'
  input.type = isPassword ? 'text' : 'password'
  btn.textContent = isPassword ? 'Hide' : 'Show'
}

function checkStrength(val) {
  const fill = document.getElementById('strength-fill')
  const label = document.getElementById('strength-label')
  if (!fill || !label) return

  let score = 0
  if (val.length >= 8) score++
  if (/[A-Z]/.test(val)) score++
  if (/[0-9]/.test(val)) score++
  if (/[^A-Za-z0-9]/.test(val)) score++

  const levels = ['', 'Weak', 'Fair', 'Good', 'Strong']
  const colors = ['', '#dc3545', '#fd7e14', '#0d6efd', '#198754']
  const widths = ['0%', '25%', '50%', '75%', '100%']

  fill.style.width = widths[score]
  fill.style.backgroundColor = colors[score]
  fill.setAttribute('aria-valuenow', String(score * 25))
  label.textContent = val.length ? levels[score] : ''
  label.style.color = colors[score]
}

document.addEventListener('DOMContentLoaded', () => {
  const passwordInput = document.getElementById('reg-password')
  if (!passwordInput) return

  passwordInput.addEventListener('input', (event) => {
    checkStrength(event.target.value)
  })
})