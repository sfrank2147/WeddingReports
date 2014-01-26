Feature: testing the wedding report site
	Scenario: check that I can log in
		When I load the login page
		And I log in
		Then I should be logged in
	
	Scenario: check that I can log out
		When I log out
		Then I should be logged out