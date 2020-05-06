describe('Home', () => {
    beforeEach(() => {
        // Because we're only testing the homepage
        // in this test file, we can run this command
        // before each individual test instead of
        // repeating it in every test.
        cy.visit('/');
    });

    it('All compnents visible', () => {
        // By using `data-qa` selectors, we can separate
        // CSS selectors used for styling from those used
        // exclusively for testing our application.
        // See: https://docs.cypress.io/guides/references/best-practices.html#Selecting-Elements
        cy.get('[data-cy=headline]').should('be.visible');
        cy.get('[data-cy=room-selection]').should('be.visible');
        cy.get('[data-cy=room-result]').should('be.visible');
        cy.get('[data-cy=room-info]').should('be.visible');
        cy.get('Raumauswahl').contains('Home');
    });
});
