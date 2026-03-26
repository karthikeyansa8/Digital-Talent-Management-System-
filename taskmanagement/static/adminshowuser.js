function showUsers() {
            // Hide the Show Users button
            const showUsersBtn = document.getElementById('showUsersBtn');
            if (showUsersBtn) {
                showUsersBtn.style.display = 'none';
            }
            
            // Show the users section
            const usersSection = document.querySelectorAll('div[style*="padding: 1.8rem"]');
            usersSection.forEach(section => {
                if (section.querySelector('h3') && section.querySelector('h3').textContent.trim() === 'All Users') {
                    section.style.display = 'block';
                }
            });
        }
        
        function hideUsers() {
            // Show the Show Users button
            const showUsersBtn = document.getElementById('showUsersBtn');
            if (showUsersBtn) {
                showUsersBtn.style.display = 'inline-flex';
            }
            
            // Hide the users section
            const usersSection = document.querySelectorAll('div[style*="padding: 1.8rem"]');
            usersSection.forEach(section => {
                if (section.querySelector('h3') && section.querySelector('h3').textContent.trim() === 'All Users') {
                    section.style.display = 'none';
                }
            });
        }