// https://docs.cypress.io/api/introduction/api.html

describe('Login Test', () => {
  beforeEach(() => {
    cy.visit('/login')
  })
  it('Visits the app root url', () => {
    cy.visit('/')
    cy.contains('h1', 'Login')
    cy.url().should('include', '/login')
  })
  it('Visits the login page directly', () => {
    cy.contains('h1', 'Login')
  })
  it('login with no credentials', () => {
    cy.contains('Anmelden').click()
    cy.url().should('include', '/login')
  })
  it('login with fake credentials', () => {
    cy.get('#login-username-input').type('fakeAccount')
    cy.get('#login-password-input').type('fakePassword', { force: true })
    cy.contains('Anmelden').click()
    cy.url().should('include', '/login')
    cy.contains('Es konnte keine Verbindung zum Server hergestellt werden. Bitte versuchen sie es später noch einmal')
  })
})
