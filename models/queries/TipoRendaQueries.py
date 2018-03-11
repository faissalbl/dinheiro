queries = {
	'find' : '''
		select id, desc, auto
		from TIPO_RENDA
        where :auto is null or auto = :auto;
	'''
}