# User Profile Functionality

A simple, responsive user profile management system built with vanilla HTML, CSS, and JavaScript.

## Features

- **View Mode**: Display user profile information including avatar, name, email, bio, and location
- **Edit Mode**: Update profile information with form validation
- **Data Persistence**: Profile data is saved to browser localStorage
- **Validation**: 
  - Email format validation
  - URL validation for avatar images
  - Required field validation (name and email)
- **Error Handling**: Graceful handling of localStorage errors and image loading failures
- **Accessibility**: ARIA attributes for screen reader support
- **Responsive Design**: Mobile-friendly interface with gradient background

## Usage

Open `profile.html` in a web browser. The profile system works entirely client-side with no server requirements.

### Viewing Your Profile

The profile displays in view mode by default, showing:
- Profile avatar
- Name
- Email address
- Bio
- Location

### Editing Your Profile

1. Click the "Edit Profile" button
2. Update any fields you wish to change
3. Click "Save Changes" to save your updates
4. Or click "Cancel" to discard changes

### Field Requirements

- **Name**: Required
- **Email**: Required (must be valid email format)
- **Bio**: Optional
- **Location**: Optional
- **Avatar URL**: Optional (must be valid URL if provided)

## Files

- `profile.html` - Main HTML structure
- `profile.css` - Styling and animations
- `profile.js` - Profile management logic

## Browser Compatibility

Works in all modern browsers that support:
- ES6 JavaScript
- localStorage API
- CSS Grid and Flexbox
