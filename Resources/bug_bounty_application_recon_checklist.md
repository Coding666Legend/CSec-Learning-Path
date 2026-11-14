# Bug Bounty --- Comprehensive Application Reconnaissance & Attack Surface Checklist

**Purpose:** Systematically enumerate an authorized public-facing web
application's functionality, entry points, data flows, identities, and
trust boundaries before vulnerability testing.

**Usage:** Check each item as it is completed. Mark irrelevant items
**N/A**. Do not test assets or techniques outside the program's explicit
authorization. This checklist is an inventory, not an instruction to
probe every item regardless of scope.

## Engagement metadata

  Field                          Value
  ------------------------------ -------
  Program / platform             
  Target / application           
  In-scope asset(s)              
  Testing account(s) / role(s)   
  ROE / policy URL               
  Testing window                 
  Rate limits / restrictions     
  Researcher notes               

## Reconnaissance and application mapping checklist

### 01. Engagement Preparation & ROE

-   [ ] Read the complete bug bounty policy
-   [ ] Identify all in-scope domains and subdomains
-   [ ] Identify explicitly authorized IP ranges
-   [ ] Identify excluded assets and third-party services
-   [ ] Document prohibited vulnerability classes
-   [ ] Document prohibited testing techniques
-   [ ] Check automated scanning restrictions
-   [ ] Check request-rate limits
-   [ ] Check account creation restrictions
-   [ ] Check social engineering restrictions
-   [ ] Check data-access and exfiltration restrictions
-   [ ] Check payment and transaction testing restrictions
-   [ ] Identify reporting and disclosure requirements
-   [ ] Record program contact and escalation process

### 02. Passive Reconnaissance

-   [ ] Identify primary domain and associated domains
-   [ ] Identify publicly known subdomains
-   [ ] Identify DNS records
-   [ ] Identify hosting and CDN providers
-   [ ] Identify web server and application technologies
-   [ ] Identify frontend frameworks
-   [ ] Identify backend frameworks where observable
-   [ ] Identify publicly exposed API documentation
-   [ ] Identify public GitHub repositories belonging to the target
-   [ ] Identify publicly indexed documents
-   [ ] Identify publicly accessible archived pages
-   [ ] Identify robots.txt
-   [ ] Identify sitemap.xml
-   [ ] Identify security.txt
-   [ ] Identify publicly exposed technology metadata
-   [ ] Identify third-party integrations
-   [ ] Identify publicly disclosed historical vulnerabilities

### 03. Website Structure & Navigation

-   [ ] Identify homepage and landing pages
-   [ ] Map all navigation menus
-   [ ] Map header and footer links
-   [ ] Identify all internal pages
-   [ ] Identify hidden or conditionally displayed pages
-   [ ] Identify redirects
-   [ ] Identify alternate language versions
-   [ ] Identify mobile-specific pages
-   [ ] Identify subdomains serving separate applications
-   [ ] Identify static content directories
-   [ ] Identify application routing patterns
-   [ ] Identify pages requiring authentication
-   [ ] Identify pages accessible without authentication
-   [ ] Identify error and fallback pages
-   [ ] Identify legacy application interfaces

### 04. Authentication & Account Management

-   [ ] Identify login functionality
-   [ ] Identify registration functionality
-   [ ] Identify logout functionality
-   [ ] Identify password reset functionality
-   [ ] Identify password change functionality
-   [ ] Identify email verification
-   [ ] Identify MFA functionality
-   [ ] Identify OAuth and SSO integrations
-   [ ] Identify account recovery workflows
-   [ ] Identify account lockout behavior
-   [ ] Identify session expiration behavior
-   [ ] Identify remember-me functionality
-   [ ] Identify account deletion functionality
-   [ ] Identify account deactivation functionality
-   [ ] Identify username and email uniqueness rules
-   [ ] Identify authentication-related API endpoints

### 05. User Roles & Authorization

-   [ ] Identify available user roles
-   [ ] Identify administrator functionality
-   [ ] Identify standard user functionality
-   [ ] Identify guest functionality
-   [ ] Identify moderator or support functionality
-   [ ] Identify role-specific dashboards
-   [ ] Identify role-specific navigation elements
-   [ ] Identify ownership-dependent resources
-   [ ] Identify organization or tenant boundaries
-   [ ] Identify invitation and membership workflows
-   [ ] Identify permission-management interfaces
-   [ ] Identify access-control enforcement points
-   [ ] Document role and permission differences

### 06. User Profile & Account Settings

-   [ ] View profile
-   [ ] Edit profile information
-   [ ] Change email address
-   [ ] Change username
-   [ ] Change password
-   [ ] Upload profile picture
-   [ ] Remove profile picture
-   [ ] Change account preferences
-   [ ] Manage notification settings
-   [ ] Manage privacy settings
-   [ ] Manage connected accounts
-   [ ] Manage API tokens if available
-   [ ] Manage active sessions
-   [ ] Manage trusted devices
-   [ ] Export personal data
-   [ ] Delete personal data

### 07. Input & Data Entry Points

-   [ ] Identify all text fields
-   [ ] Identify search fields
-   [ ] Identify URL parameters
-   [ ] Identify form parameters
-   [ ] Identify hidden form fields
-   [ ] Identify dropdowns
-   [ ] Identify radio buttons
-   [ ] Identify checkboxes
-   [ ] Identify rich-text editors
-   [ ] Identify comment fields
-   [ ] Identify feedback forms
-   [ ] Identify contact forms
-   [ ] Identify date and time inputs
-   [ ] Identify numeric inputs
-   [ ] Identify file upload inputs
-   [ ] Identify JSON-based inputs
-   [ ] Identify client-side validation rules
-   [ ] Identify server-side validation behavior

### 08. URL & Parameter Mapping

-   [ ] Record all discovered URLs
-   [ ] Record HTTP methods
-   [ ] Identify query parameters
-   [ ] Identify path parameters
-   [ ] Identify resource identifiers
-   [ ] Identify pagination parameters
-   [ ] Identify sorting parameters
-   [ ] Identify filtering parameters
-   [ ] Identify redirect parameters
-   [ ] Identify language and locale parameters
-   [ ] Identify optional parameters
-   [ ] Identify repeated parameters
-   [ ] Identify parameter encoding behavior
-   [ ] Identify endpoints accepting JSON
-   [ ] Identify endpoints accepting multipart/form-data

### 09. API Attack Surface

-   [ ] Identify REST API endpoints
-   [ ] Identify GraphQL endpoints if present
-   [ ] Identify API versions
-   [ ] Identify API authentication mechanisms
-   [ ] Identify API authorization requirements
-   [ ] Identify API request methods
-   [ ] Identify API response structures
-   [ ] Identify API pagination
-   [ ] Identify API filtering and sorting
-   [ ] Identify API rate-limit behavior
-   [ ] Identify API error responses
-   [ ] Identify API documentation
-   [ ] Identify WebSocket functionality
-   [ ] Identify webhook functionality
-   [ ] Identify API endpoints used by mobile applications if in scope
-   [ ] Identify deprecated API versions

### 10. File Upload & Download

-   [ ] Identify all upload functionality
-   [ ] Identify accepted file extensions
-   [ ] Identify accepted MIME types
-   [ ] Identify maximum file sizes
-   [ ] Identify image upload functionality
-   [ ] Identify document upload functionality
-   [ ] Identify archive upload functionality
-   [ ] Identify file replacement functionality
-   [ ] Identify file deletion functionality
-   [ ] Identify file download functionality
-   [ ] Identify file preview functionality
-   [ ] Identify file processing functionality
-   [ ] Identify file ownership controls
-   [ ] Identify storage and access patterns
-   [ ] Identify public versus private file access

### 11. Search & Filtering

-   [ ] Identify global search
-   [ ] Identify product or content search
-   [ ] Identify user search
-   [ ] Identify advanced search
-   [ ] Identify autocomplete functionality
-   [ ] Identify search suggestions
-   [ ] Identify filters
-   [ ] Identify sorting options
-   [ ] Identify pagination
-   [ ] Identify search history
-   [ ] Identify saved searches
-   [ ] Identify search API endpoints
-   [ ] Identify search result access controls

### 12. Business Logic & Workflows

-   [ ] Map registration workflows
-   [ ] Map account verification workflows
-   [ ] Map invitation workflows
-   [ ] Map approval workflows
-   [ ] Map subscription workflows
-   [ ] Map checkout workflows
-   [ ] Map payment workflows
-   [ ] Map refund workflows
-   [ ] Map cancellation workflows
-   [ ] Map order-management workflows
-   [ ] Map coupon and discount workflows
-   [ ] Map points and rewards workflows
-   [ ] Map booking and reservation workflows
-   [ ] Map inventory workflows
-   [ ] Map workflow state transitions
-   [ ] Identify actions requiring multiple sequential steps
-   [ ] Identify workflows involving multiple users

### 13. E-commerce & Payment Functionality

-   [ ] Identify product listing
-   [ ] Identify product details
-   [ ] Identify shopping cart
-   [ ] Identify quantity modification
-   [ ] Identify checkout process
-   [ ] Identify shipping address management
-   [ ] Identify billing address management
-   [ ] Identify payment methods
-   [ ] Identify payment confirmation
-   [ ] Identify coupon application
-   [ ] Identify discounts and promotions
-   [ ] Identify subscription management
-   [ ] Identify order history
-   [ ] Identify order cancellation
-   [ ] Identify refunds
-   [ ] Identify invoices and receipts
-   [ ] Identify payment gateway integrations

### 14. Content Management & User-Generated Content

-   [ ] Identify comments
-   [ ] Identify reviews and ratings
-   [ ] Identify discussion forums
-   [ ] Identify messaging functionality
-   [ ] Identify direct messages
-   [ ] Identify profile descriptions
-   [ ] Identify blog or article publishing
-   [ ] Identify rich-text content editors
-   [ ] Identify HTML rendering behavior
-   [ ] Identify content moderation functionality
-   [ ] Identify content deletion and editing
-   [ ] Identify attachment functionality
-   [ ] Identify content visibility settings

### 15. Client-Side Attack Surface

-   [ ] Identify JavaScript files
-   [ ] Identify frontend routing
-   [ ] Identify client-side authentication state
-   [ ] Identify browser storage usage
-   [ ] Identify localStorage usage
-   [ ] Identify sessionStorage usage
-   [ ] Identify cookie usage
-   [ ] Identify client-side API configuration
-   [ ] Identify exposed source maps
-   [ ] Identify frontend environment configuration
-   [ ] Identify sensitive information exposed in frontend responses
-   [ ] Identify client-side validation
-   [ ] Identify DOM manipulation points
-   [ ] Identify third-party JavaScript dependencies
-   [ ] Identify cross-origin resource loading

### 16. Session & Cookie Inventory

-   [ ] Record session cookie names
-   [ ] Record cookie attributes
-   [ ] Identify HttpOnly attributes
-   [ ] Identify Secure attributes
-   [ ] Identify SameSite attributes
-   [ ] Identify session creation behavior
-   [ ] Identify session rotation behavior
-   [ ] Identify session invalidation behavior
-   [ ] Identify logout behavior
-   [ ] Identify concurrent session behavior
-   [ ] Identify persistent authentication tokens
-   [ ] Identify refresh-token workflows
-   [ ] Identify CSRF token mechanisms

### 17. Security Headers & Transport

-   [ ] Record HTTPS behavior
-   [ ] Identify HTTP-to-HTTPS redirects
-   [ ] Inspect HSTS configuration
-   [ ] Inspect Content-Security-Policy
-   [ ] Inspect X-Frame-Options or frame-ancestors
-   [ ] Inspect X-Content-Type-Options
-   [ ] Inspect Referrer-Policy
-   [ ] Inspect Permissions-Policy
-   [ ] Inspect CORS configuration
-   [ ] Inspect cache-control behavior
-   [ ] Inspect TLS configuration
-   [ ] Identify mixed-content resources

### 18. Error Handling & Information Disclosure

-   [ ] Identify application error pages
-   [ ] Identify server error responses
-   [ ] Identify validation error responses
-   [ ] Identify authentication error responses
-   [ ] Identify authorization error responses
-   [ ] Identify stack traces if exposed
-   [ ] Identify debug information if exposed
-   [ ] Identify software version disclosures
-   [ ] Identify verbose API errors
-   [ ] Identify sensitive information in responses
-   [ ] Identify directory listing exposure
-   [ ] Identify unintended public configuration files

### 19. Third-Party Integrations

-   [ ] Identify OAuth providers
-   [ ] Identify payment providers
-   [ ] Identify analytics integrations
-   [ ] Identify customer support integrations
-   [ ] Identify cloud storage integrations
-   [ ] Identify external authentication services
-   [ ] Identify embedded third-party content
-   [ ] Identify external API dependencies
-   [ ] Identify webhook integrations
-   [ ] Identify cross-domain communication
-   [ ] Verify whether third-party assets are in scope before testing
    them

### 20. Administrative Functionality

-   [ ] Identify admin login interfaces
-   [ ] Identify admin dashboards
-   [ ] Identify user management
-   [ ] Identify role management
-   [ ] Identify permission management
-   [ ] Identify moderation interfaces
-   [ ] Identify audit logs
-   [ ] Identify administrative search
-   [ ] Identify configuration interfaces
-   [ ] Identify system settings
-   [ ] Identify administrative API endpoints
-   [ ] Identify privileged operations
-   [ ] Identify administrative workflows

### 21. Multi-Tenant Functionality

-   [ ] Identify organization creation
-   [ ] Identify organization membership
-   [ ] Identify tenant-specific dashboards
-   [ ] Identify tenant-specific resources
-   [ ] Identify organization invitations
-   [ ] Identify tenant switching
-   [ ] Identify tenant administration
-   [ ] Identify cross-tenant data boundaries
-   [ ] Identify organization-level permissions
-   [ ] Identify shared resources

### 22. Real-Time & Communication Features

-   [ ] Identify WebSocket connections
-   [ ] Identify live notifications
-   [ ] Identify real-time dashboards
-   [ ] Identify chat functionality
-   [ ] Identify messaging functionality
-   [ ] Identify video or audio functionality
-   [ ] Identify event-stream endpoints
-   [ ] Identify push notifications
-   [ ] Identify presence indicators
-   [ ] Identify real-time collaboration features

### 23. Infrastructure & Deployment Surface

-   [ ] Identify CDN behavior
-   [ ] Identify reverse proxy behavior
-   [ ] Identify load-balancer behavior where observable
-   [ ] Identify origin-host exposure where publicly observable
-   [ ] Identify public cloud storage references
-   [ ] Identify exposed development environments
-   [ ] Identify exposed staging environments
-   [ ] Identify exposed test environments
-   [ ] Identify legacy hosts
-   [ ] Identify alternate application entry points
-   [ ] Identify publicly accessible health endpoints
-   [ ] Identify publicly accessible status endpoints

### 24. Vulnerability Testing Preparation

-   [ ] Map features to relevant vulnerability classes
-   [ ] Identify authentication testing candidates
-   [ ] Identify authorization testing candidates
-   [ ] Identify IDOR/BOLA testing candidates
-   [ ] Identify injection testing candidates
-   [ ] Identify XSS testing candidates
-   [ ] Identify CSRF testing candidates
-   [ ] Identify SSRF testing candidates
-   [ ] Identify file-handling testing candidates
-   [ ] Identify business-logic testing candidates
-   [ ] Identify session-management testing candidates
-   [ ] Identify API security testing candidates
-   [ ] Identify misconfiguration testing candidates
-   [ ] Prioritize high-impact attack surfaces
-   [ ] Confirm each test is permitted by the ROE

### 25. Evidence & Reporting Preparation

-   [ ] Create engagement directory
-   [ ] Create application map
-   [ ] Create endpoint inventory
-   [ ] Create account and role inventory
-   [ ] Create testing tracker
-   [ ] Record timestamps
-   [ ] Save relevant HTTP requests and responses
-   [ ] Capture screenshots where useful
-   [ ] Record affected endpoints
-   [ ] Record affected parameters
-   [ ] Record authentication requirements
-   [ ] Record reproduction prerequisites
-   [ ] Record observed impact
-   [ ] Separate confirmed findings from hypotheses
-   [ ] Remove unnecessary sensitive data from evidence
-   [ ] Prepare reproducible proof of concept
-   [ ] Check program reporting requirements

## 26. Vulnerability testing taxonomy

  -----------------------------------------------------------------------
  Vulnerability category              Areas to investigate
  ----------------------------------- -----------------------------------
  Broken Access Control               IDOR, BOLA, privilege escalation,
                                      missing function-level
                                      authorization

  Authentication                      Authentication weaknesses, MFA
                                      flaws, account recovery flaws

  Session Management                  Session fixation, improper
                                      invalidation, token lifecycle
                                      issues

  Injection                           SQL injection, NoSQL injection,
                                      command injection, template
                                      injection

  Cross-Site Scripting                Reflected, stored, and DOM-based
                                      XSS

  CSRF                                Unauthorized state-changing actions

  SSRF                                Server-side outbound request
                                      functionality

  File Handling                       Upload validation, path traversal,
                                      unsafe processing

  Business Logic                      Workflow bypass, price or quantity
                                      manipulation, state-transition
                                      flaws

  API Security                        BOLA, broken authentication,
                                      excessive data exposure, mass
                                      assignment

  Security Misconfiguration           CORS, security headers, exposed
                                      services or configuration

  Information Disclosure              Sensitive data exposure and
                                      unintended metadata leakage

  Cryptographic Failures              Improper handling or protection of
                                      sensitive data

  Race Conditions                     Concurrent transaction and workflow
                                      issues
  -----------------------------------------------------------------------

Only test applicable vulnerability classes and only where permitted by
the program policy. Avoid destructive actions, unnecessary access to
other users' data, and actions that could affect availability or real
transactions.

## 27. Suggested engagement directory

``` text
Bug-Bounty-Engagement/
├── 00-Engagement/
│   ├── ROE.md
│   ├── Scope.md
│   └── Restrictions.md
├── 01-Reconnaissance/
│   ├── Domains.md
│   ├── Subdomains.md
│   ├── Technologies.md
│   └── Public-Information.md
├── 02-Application-Mapping/
│   ├── Site-Structure.md
│   ├── Functionality.md
│   ├── User-Roles.md
│   ├── Workflows.md
│   └── Attack-Surface.md
├── 03-Endpoint-Inventory/
│   ├── Endpoints.md
│   ├── API.md
│   ├── Parameters.md
│   └── Authentication.md
├── 04-Testing/
│   ├── Authentication.md
│   ├── Authorization.md
│   ├── Injection.md
│   ├── Business-Logic.md
│   ├── API-Security.md
│   └── Testing-Tracker.md
├── 05-Evidence/
│   ├── Requests/
│   ├── Responses/
│   └── Screenshots/
└── 06-Reports/
    ├── Findings.md
    └── Final-Report.md
```

## 28. Endpoint inventory template

  Field                             Details
  --------------------------------- ------------------------------------------
  Endpoint                          
  HTTP method                       
  Feature / workflow                
  Authentication required           
  User role / ownership context     
  Parameters / request body         
  Content type                      
  Response / status code            
  Sensitive data involved           
  Authorization boundary            
  ROE constraints                   
  Potential vulnerability classes   
  Testing status                    Not started / In progress / Tested / N/A
  Evidence reference                
  Notes                             

## 29. Testing tracker template

  ---------------------------------------------------------------------------
  Feature        Endpoint(s)    Vulnerability   Status         Evidence /
                                class                          notes
  -------------- -------------- --------------- -------------- --------------
                                                Pending        

                                                Pending        

                                                Pending        
  ---------------------------------------------------------------------------

Suggested statuses: **Not started**, **In progress**, **Tested --- no
issue observed**, **Finding confirmed**, **N/A**, **Blocked by ROE**.

## 30. Evidence and finding record template

### Finding title

-   **Affected asset / endpoint:**
-   **Vulnerability class:**
-   **Severity (proposed):**
-   **Date and time (timezone):**
-   **Required role / account:**
-   **Preconditions:**
-   **Steps to reproduce:**
-   **Expected result:**
-   **Actual result:**
-   **Security impact:**
-   **Evidence references:**
-   **ROE / policy considerations:**
-   **Remediation suggestion:**

Do not include unnecessary personal data, secrets, or unrelated user
records in evidence. Redact sensitive values while retaining enough
information for the program to validate the finding.

## Operating principles

1.  **Map before testing:** Understand the feature, endpoint, inputs,
    identity context, and authorization boundary.
2.  **Separate observation from validation:** A suspicious response or
    exposed field is a lead, not automatically a vulnerability.
3.  **Use controlled accounts:** Where possible, use accounts you own
    and roles explicitly permitted by the program.
4.  **Minimize impact:** Avoid destructive changes, bulk extraction,
    denial-of-service testing, and real financial transactions unless
    explicitly authorized.
5.  **Respect scope at every layer:** A first-party page may load
    third-party services that are not in scope.
6.  **Keep reproducible evidence:** Record the request, response,
    prerequisites, timestamp, and impact without collecting unnecessary
    sensitive data.
7.  **Prioritize intelligently:** Focus on sensitive data, authorization
    boundaries, privileged actions, and high-value business workflows
    rather than checking boxes mechanically.

**Core mapping relationship:**
`Functionality → Endpoint → Input → Identity / role → Authorization boundary → Potential vulnerability class`.
