
CREATE TABLE gdpr_policies (
    policy_id SERIAL PRIMARY KEY,
    policy_name VARCHAR(100),
    description TEXT
);

INSERT INTO gdpr_policies (policy_name, description) VALUES
('Right to Access', 'Users can request access to their data.'),
('Right to Erasure', 'Users can request deletion of their data.');
