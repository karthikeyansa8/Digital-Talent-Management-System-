function togglePass(id, btn) {
      const input = document.getElementById(id);
      input.type = input.type === 'password' ? 'text' : 'password';
      btn.classList.toggle('active');
    }
    // Input focus animation
    document.querySelectorAll('.field-input').forEach(input => {
      input.addEventListener('focus', () => input.closest('.field-wrap').classList.add('focused'));
      input.addEventListener('blur', () => input.closest('.field-wrap').classList.remove('focused'));
    });