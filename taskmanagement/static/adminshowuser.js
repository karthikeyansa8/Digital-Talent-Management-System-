function showUsers() {
            // Hide the Show Users button
            const showUsersBtn = document.getElementById('showUsersBtn');
            if (showUsersBtn) {
                showUsersBtn.style.display = 'none';
            }
            
            // Show the users section
            const usersSection = document.getElementById('usersSection');
            if (usersSection) {
                usersSection.style.display = 'block';
            }
        }
        
        function hideUsers() {
            // Show the Show Users button
            const showUsersBtn = document.getElementById('showUsersBtn');
            if (showUsersBtn) {
                showUsersBtn.style.display = 'inline-flex';
            }
            
            // Hide the users section
            const usersSection = document.getElementById('usersSection');
            if (usersSection) {
                usersSection.style.display = 'none';
            }
        }