import { betterAuth } from "better-auth";
import { createAuthClient } from "better-auth/react"

export const authClient = createAuthClient ({
  baseURL: process.env.BETTER_AUTH_URL || '',
});


class AuthService {
  signup() {
    // TODO: Implement Better Auth signup
    console.log("Signing up...");
    // After successful signup, redirect to the profile page
    window.location.href = '/profile';
  }

  signin() {
    // TODO: Implement Better Auth signin
    console.log("Signing in...");
  }
}

export default new AuthService();
