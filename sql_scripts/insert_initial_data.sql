INSERT INTO CLIENT (id, name, email)
VALUES 
	(1, "Bernardinho", "bernardinho@volei.com"),
	(2, "Sheila", "sheila@volei.com"),
	(3, "Giba", "giba@volei.com"),
	(4, "Mari", "mari@volei.com");


INSERT INTO GYM (id, name, address)
VALUES 
	(1, "CleverFit", "Santos Dummont Street"),
	(2, "VidaFisic", "Albert Einstein Avenue"),
	(3, "BodyFit", "Marie Curie Street");
	
INSERT INTO MODALITY (id, name)
VALUES 
	(1, "Spinning"),
	(2, "Boxe"),
	(3, "Weight training"),
	(4, "Zumba");
	
INSERT INTO CLIENT_GYM (id, client_id, gym_id)
VALUES 
	(1, 1, 2),
	(2, 1, 3),
	(3, 2, 1),
	(4, 2, 3), 
	(5, 3, 2),
	(6, 3, 1),
	(7, 4, 3);
	
INSERT INTO GYM_MODALITY (id, gym_id, modality_id)
VALUES 
	(1, 1, 1),
	(2, 1, 3),
	(3, 2, 2),
	(4, 2, 4), 
	(5, 3, 1),
	(6, 3, 2),
	(7, 3, 4);
	
INSERT INTO CLIENT_MODALITY (id, client_id, modality_id)
VALUES 
	(1, 1, 2),
	(2, 1, 1),
	(3, 2, 3),
	(4, 2, 4), 
	(5, 3, 4),
	(6, 3, 1),
	(7, 4, 2);
	