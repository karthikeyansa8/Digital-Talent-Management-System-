function togglePass(id, btn) {
        const input = document.getElementById(id)
        input.type = input.type === 'password' ? 'text' : 'password'
        btn.classList.toggle('active')
      }
      
      function checkStrength(val) {
        const fill = document.getElementById('strength-fill')
        const label = document.getElementById('strength-label')
        let score = 0
        if (val.length >= 8) score++
        if (/[A-Z]/.test(val)) score++
        if (/[0-9]/.test(val)) score++
        if (/[^A-Za-z0-9]/.test(val)) score++
        const levels = ['', 'Weak', 'Fair', 'Good', 'Strong']
        const colors = ['', '#e74c3c', '#f39c12', '#3498db', '#27ae60']
        const widths = ['0%', '25%', '50%', '75%', '100%']
        fill.style.width = widths[score]
        fill.style.background = colors[score]
        label.textContent = val.length ? levels[score] : ''
        label.style.color = colors[score]
      }
      
      document.querySelectorAll('.field-input').forEach((input) => {
        input.addEventListener('focus', () => input.closest('.field-wrap').classList.add('focused'))
        input.addEventListener('blur', () => input.closest('.field-wrap').classList.remove('focused'))
      })