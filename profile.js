// User profile management
class UserProfile {
    constructor() {
        this.defaultProfile = {
            name: 'John Doe',
            email: 'john.doe@example.com',
            bio: 'Software developer passionate about coding.',
            location: 'San Francisco, CA',
            avatar: 'https://via.placeholder.com/150'
        };
        
        this.initElements();
        this.loadProfile();
        this.attachEventListeners();
    }

    initElements() {
        // View mode elements
        this.viewMode = document.getElementById('view-mode');
        this.editMode = document.getElementById('edit-mode');
        this.nameDisplay = document.getElementById('name-display');
        this.emailDisplay = document.getElementById('email-display');
        this.bioDisplay = document.getElementById('bio-display');
        this.locationDisplay = document.getElementById('location-display');
        this.avatarDisplay = document.getElementById('avatar-display');
        
        // Edit mode elements
        this.profileForm = document.getElementById('profile-form');
        this.nameInput = document.getElementById('name-input');
        this.emailInput = document.getElementById('email-input');
        this.bioInput = document.getElementById('bio-input');
        this.locationInput = document.getElementById('location-input');
        this.avatarInput = document.getElementById('avatar-input');
        
        // Buttons
        this.editBtn = document.getElementById('edit-btn');
        this.cancelBtn = document.getElementById('cancel-btn');
    }

    attachEventListeners() {
        this.editBtn.addEventListener('click', () => this.showEditMode());
        this.cancelBtn.addEventListener('click', () => this.showViewMode());
        this.profileForm.addEventListener('submit', (e) => this.saveProfile(e));
    }

    loadProfile() {
        try {
            const savedProfile = localStorage.getItem('userProfile');
            const profile = savedProfile ? JSON.parse(savedProfile) : this.defaultProfile;
            
            this.displayProfile(profile);
        } catch (error) {
            console.error('Error loading profile:', error);
            this.displayProfile(this.defaultProfile);
        }
    }

    displayProfile(profile) {
        this.nameDisplay.textContent = profile.name;
        this.emailDisplay.textContent = profile.email;
        this.bioDisplay.textContent = profile.bio;
        this.locationDisplay.textContent = profile.location;
        this.avatarDisplay.src = profile.avatar;
        this.avatarDisplay.alt = `${profile.name}'s profile picture`;
        
        // Handle image loading errors
        this.avatarDisplay.onerror = () => {
            this.avatarDisplay.src = this.defaultProfile.avatar;
        };
    }

    showEditMode() {
        try {
            const savedProfile = localStorage.getItem('userProfile');
            const profile = savedProfile ? JSON.parse(savedProfile) : this.defaultProfile;
            
            this.nameInput.value = profile.name;
            this.emailInput.value = profile.email;
            this.bioInput.value = profile.bio;
            this.locationInput.value = profile.location;
            this.avatarInput.value = profile.avatar;
            
            this.viewMode.style.display = 'none';
            this.viewMode.setAttribute('aria-hidden', 'true');
            this.editMode.style.display = 'block';
            this.editMode.setAttribute('aria-hidden', 'false');
        } catch (error) {
            console.error('Error loading profile for editing:', error);
            this.showErrorMessage('Failed to load profile for editing.');
        }
    }

    showViewMode() {
        this.viewMode.style.display = 'block';
        this.viewMode.setAttribute('aria-hidden', 'false');
        this.editMode.style.display = 'none';
        this.editMode.setAttribute('aria-hidden', 'true');
    }

    saveProfile(e) {
        e.preventDefault();
        
        const profile = {
            name: this.nameInput.value.trim(),
            email: this.emailInput.value.trim(),
            bio: this.bioInput.value.trim(),
            location: this.locationInput.value.trim(),
            avatar: this.avatarInput.value.trim() || this.defaultProfile.avatar
        };

        // Validate name
        if (!profile.name) {
            this.showErrorMessage('Name is required.');
            return;
        }

        // Validate email
        if (!this.isValidEmail(profile.email)) {
            this.showErrorMessage('Please enter a valid email address.');
            return;
        }

        // Validate avatar URL
        if (this.avatarInput.value.trim() && !this.isValidUrl(profile.avatar)) {
            this.showErrorMessage('Please enter a valid URL for the avatar.');
            return;
        }

        // Save to localStorage
        try {
            localStorage.setItem('userProfile', JSON.stringify(profile));
        } catch (error) {
            console.error('Error saving profile:', error);
            this.showErrorMessage('Failed to save profile. Please try again.');
            return;
        }
        
        // Update display
        this.displayProfile(profile);
        this.showViewMode();
        
        // Show success message
        this.showSuccessMessage();
    }

    isValidEmail(email) {
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return emailRegex.test(email);
    }

    isValidUrl(url) {
        try {
            new URL(url);
            return true;
        } catch {
            return false;
        }
    }

    showSuccessMessage() {
        this.showMessage('Profile updated successfully!', '#4caf50');
    }

    showErrorMessage(text) {
        this.showMessage(text, '#f44336');
    }

    showMessage(text, backgroundColor) {
        const message = document.createElement('div');
        message.textContent = text;
        message.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${backgroundColor};
            color: white;
            padding: 15px 25px;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            z-index: 1000;
            animation: slideIn 0.3s ease-out;
        `;
        
        document.body.appendChild(message);
        
        setTimeout(() => {
            message.style.animation = 'slideOut 0.3s ease-in';
            setTimeout(() => message.remove(), 300);
        }, 3000);
    }
}

// Initialize the profile manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new UserProfile();
});
