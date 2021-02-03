Search.setIndex({docnames:["index","introduction/acknowledgements","introduction/bibliography","introduction/configuration","introduction/databases","introduction/datasets","introduction/dependencies","introduction/execution","introduction/faults","introduction/index","introduction/introduction","introduction/requirements","launcher","modules","setup","sugaroid","sugaroid.backend","sugaroid.brain","sugaroid.cli","sugaroid.config","sugaroid.game","sugaroid.google","sugaroid.gui","sugaroid.platform","sugaroid.reader","sugaroid.trainer","sugaroid.translator","sugaroid.trivia","sugaroid.tts"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":3,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":2,"sphinx.domains.rst":2,"sphinx.domains.std":1,"sphinx.ext.todo":2,"sphinx.ext.viewcode":1,sphinx:56},filenames:["index.rst","introduction/acknowledgements.rst","introduction/bibliography.rst","introduction/configuration.rst","introduction/databases.rst","introduction/datasets.rst","introduction/dependencies.rst","introduction/execution.rst","introduction/faults.rst","introduction/index.rst","introduction/introduction.rst","introduction/requirements.rst","launcher.rst","modules.rst","setup.rst","sugaroid.rst","sugaroid.backend.rst","sugaroid.brain.rst","sugaroid.cli.rst","sugaroid.config.rst","sugaroid.game.rst","sugaroid.google.rst","sugaroid.gui.rst","sugaroid.platform.rst","sugaroid.reader.rst","sugaroid.trainer.rst","sugaroid.translator.rst","sugaroid.trivia.rst","sugaroid.tts.rst"],objects:{"":{launcher:[12,0,0,"-"],setup:[14,0,0,"-"],sugaroid:[15,0,0,"-"]},"sugaroid.backend":{sql:[16,0,0,"-"]},"sugaroid.backend.sql":{PossibleSQLInjectionPanicError:[16,1,1,""],SqlDatabaseManagement:[16,2,1,""],convert_data_escaped_string:[16,4,1,""]},"sugaroid.backend.sql.SqlDatabaseManagement":{append:[16,3,1,""],close:[16,3,1,""],database_path:[16,3,1,""],table:[16,3,1,""]},"sugaroid.brain":{brain:[17,0,0,"-"],constants:[17,0,0,"-"],idk:[17,0,0,"-"],ooo:[17,0,0,"-"],postprocessor:[17,0,0,"-"],preprocessors:[17,0,0,"-"],utils:[17,0,0,"-"]},"sugaroid.brain.brain":{Neuron:[17,2,1,""]},"sugaroid.brain.brain.Neuron":{alu:[17,3,1,""],gen_arithmetic:[17,3,1,""],gen_best_match:[17,3,1,""],gen_time:[17,3,1,""],normalize:[17,3,1,""],parse:[17,3,1,""],time:[17,3,1,""]},"sugaroid.brain.ooo":{Emotion:[17,2,1,""]},"sugaroid.brain.ooo.Emotion":{adorable:[17,5,1,""],angel:[17,5,1,""],angry:[17,5,1,""],angry_non_expressive:[17,5,1,""],blush:[17,5,1,""],cry:[17,5,1,""],cry_overflow:[17,5,1,""],dead:[17,5,1,""],depressed:[17,5,1,""],fun:[17,5,1,""],genie:[17,5,1,""],github:[17,5,1,""],lol:[17,5,1,""],negative:[17,5,1,""],neutral:[17,5,1,""],non_expressive:[17,5,1,""],non_expressive_left:[17,5,1,""],o:[17,5,1,""],positive:[17,5,1,""],rich:[17,5,1,""],seriously:[17,5,1,""],sleep:[17,5,1,""],smirking:[17,5,1,""],vomit:[17,5,1,""],wink:[17,5,1,""]},"sugaroid.brain.postprocessor":{any_in:[17,4,1,""],cosine_similarity:[17,4,1,""],difference:[17,4,1,""],lemma_in:[17,4,1,""],pos_in:[17,4,1,""],random_response:[17,4,1,""],raw_in:[17,4,1,""],raw_lower_in:[17,4,1,""],reverse:[17,4,1,""],sigmaSimilarity:[17,4,1,""],text2int:[17,4,1,""]},"sugaroid.brain.preprocessors":{current_time:[17,4,1,""],non_punkt_normalize:[17,4,1,""],normalize:[17,4,1,""],preprocess:[17,4,1,""],purify:[17,4,1,""],spac_token:[17,4,1,""],tokenize:[17,4,1,""]},"sugaroid.brain.utils":{LanguageProcessor:[17,2,1,""]},"sugaroid.brain.utils.LanguageProcessor":{lemma:[17,3,1,""],lp:[17,3,1,""],similarity:[17,3,1,""],tokenize:[17,3,1,""]},"sugaroid.cli":{cli:[18,0,0,"-"]},"sugaroid.cli.cli":{SugaroidCLIWrapper:[18,2,1,""]},"sugaroid.cli.cli.SugaroidCLIWrapper":{get:[18,3,1,""],put:[18,3,1,""]},"sugaroid.config":{config:[19,0,0,"-"]},"sugaroid.config.config":{ConfigManager:[19,2,1,""]},"sugaroid.config.config.ConfigManager":{check_file:[19,3,1,""],get_cfgpath:[19,3,1,""],get_config:[19,3,1,""],read_file:[19,3,1,""],reset_config:[19,3,1,""],update_config:[19,3,1,""],write_file:[19,3,1,""]},"sugaroid.game":{game:[20,0,0,"-"]},"sugaroid.game.game":{game_file:[20,4,1,""]},"sugaroid.platform":{darwin:[23,0,0,"-"],linux:[23,0,0,"-"],platform:[23,0,0,"-"],windows:[23,0,0,"-"]},"sugaroid.platform.darwin":{Darwin:[23,2,1,""]},"sugaroid.platform.darwin.Darwin":{cfgpath:[23,3,1,""],increment:[23,3,1,""],make_config:[23,3,1,""],paths:[23,3,1,""],system:[23,3,1,""]},"sugaroid.platform.linux":{Linux:[23,2,1,""]},"sugaroid.platform.linux.Linux":{cfgpath:[23,3,1,""],increment:[23,3,1,""],make_config:[23,3,1,""],paths:[23,3,1,""],system:[23,3,1,""]},"sugaroid.platform.windows":{Windows:[23,2,1,""]},"sugaroid.platform.windows.Windows":{cfgpath:[23,3,1,""],increment:[23,3,1,""],make_config:[23,3,1,""],paths:[23,3,1,""],system:[23,3,1,""]},"sugaroid.reader":{markdown:[24,0,0,"-"],rst:[24,0,0,"-"],scrawled:[24,0,0,"-"]},"sugaroid.train":{SugaroidTrainer:[15,2,1,""]},"sugaroid.trainer":{trainer:[25,0,0,"-"]},"sugaroid.trainer.trainer":{SugaroidTrainer:[25,2,1,""],main:[25,4,1,""]},"sugaroid.trainer.trainer.SugaroidTrainer":{modify:[25,3,1,""],prompt_cli:[25,3,1,""],reset:[25,3,1,""],train:[25,3,1,""],trainer_cli:[25,3,1,""],trainer_init:[25,3,1,""],write:[25,3,1,""]},"sugaroid.trivia":{trivia:[27,0,0,"-"],triviadb:[27,0,0,"-"]},"sugaroid.trivia.trivia":{SugaroidTrivia:[27,2,1,""]},"sugaroid.trivia.trivia.SugaroidTrivia":{answer:[27,3,1,""],ask:[27,3,1,""]},"sugaroid.tts":{mic:[28,0,0,"-"]},sugaroid:{backend:[16,0,0,"-"],brain:[17,0,0,"-"],cli:[18,0,0,"-"],config:[19,0,0,"-"],game:[20,0,0,"-"],google:[21,0,0,"-"],gui:[22,0,0,"-"],platform:[23,0,0,"-"],reader:[24,0,0,"-"],train:[15,0,0,"-"],trainer:[25,0,0,"-"],translator:[26,0,0,"-"],trivia:[27,0,0,"-"],tts:[28,0,0,"-"],version:[15,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","exception","Python exception"],"2":["py","class","Python class"],"3":["py","method","Python method"],"4":["py","function","Python function"],"5":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:exception","2":"py:class","3":"py:method","4":"py:function","5":"py:attribute"},terms:{"03822":2,"1024":11,"1806":2,"2019":1,"2020":[15,17,18,19,23,25,26,27,28],"2021":[15,17,18,19,23,25,26,27,28],"493174":17,"600":11,"8000":7,"93shannon_diverg":2,"case":[3,4,16],"class":[12,14,15,16,17,18,19,23,25,27],"default":[5,12,14],"final":17,"function":[6,12,14],"import":[5,10],"new":[6,7,10,12,13,14,15],"public":[19,23],"return":[12,14,16,17,20],"short":17,"static":[17,23,25],"true":20,"var":17,AND:[15,17,18,19,23,25,26,27,28],AWS:4,And:4,BUT:[15,17,18,19,23,25,26,27,28],FOR:[15,17,18,19,23,25,26,27,28],For:[4,11],Its:5,NOT:[15,17,18,19,23,25,26,27,28],Such:8,THE:[15,17,18,19,23,25,26,27,28],TTS:3,The:[3,4,8,10,12,14,15,17,18,19,23,25,26,27,28],There:[3,4,6,7],These:[3,5,12,14],USE:[15,17,18,19,23,25,26,27,28],Used:6,Useful:[12,14],Using:4,WITH:[15,17,18,19,23,25,26,27,28],__class__:[12,14],abl:7,about:[13,15],abov:[15,17,18,19,23,25,26,27,28],abs:2,access:[12,14],accord:3,accordingli:3,accur:[5,8],accuraci:5,acknowledg:[0,9],across:1,act:[12,14],action:[15,17,18,19,23,25,26,27,28],activ:10,adapt:[4,8],add:6,adding:[1,4],addit:3,address:7,ador:17,advanc:17,after:[12,14],against:4,aim:10,aka:[1,5],aki:[13,15],akin:6,algorithm:[4,8],all:[4,15,17,18,19,23,25,26,27,28],allow:[6,12,14],alon:4,along:[1,4,19,23],also:[1,3,4,12,14],alter:16,alu:17,alwai:10,amd:11,analyz:[4,5],andrea:1,andreagon:1,angel:17,angri:17,angry_non_express:17,ani:[7,11,12,14,15,17,18,19,23,25,26,27,28],anil:1,anoth:[4,6],answer:[2,3,4,8,27],any_in:17,apart:4,api:6,app:4,appdata:[3,4],append:[4,16],appli:7,appropri:6,approxim:[5,8],arbitrari:[12,14],arey:[13,15],arg1:17,arg2:17,arg:17,argument:[3,7,12,14,17],aris:[15,17,18,19,23,25,26,27,28],arrai:5,artifici:[5,10,15,17,18,19,23,25,26,27,28],arxiv:2,ask:27,assert:[13,15],assist:10,associ:[15,17,18,19,23,25,26,27,28],attempt:[12,14,16],attribut:[4,12,14],attributeerror:[12,14],audio:[3,7],author:[15,17,18,19,23,25,26,27,28],avail:[2,4],averaged_perceptron_tagg:5,azra:1,azur:[1,4,10],backend:[4,13,15],base:[6,15,16,17,18,19,23,25,27],basic:6,bay:2,bayer:4,beautifulsoup4:6,becaus:[4,8,13,15],becom:[1,4],been:8,behaviour:[12,14],being:10,benefit:10,best:5,beta:10,bibliographi:[0,9],binari:4,blush:17,bot:[2,3,4,5,6,8,10,17],brain:[3,5,13,15],browser:7,bsd:11,bug:1,built:10,button:10,bye:[13,15],call:[8,12,14],can:[4,5,7,12,14,19,23],canmai:[13,15],capit:17,certain:[4,6,17],cfgpath:23,chacko:1,chang:[12,14,16],channel:4,charact:17,charg:[7,15,17,18,19,23,25,26,27,28],chat:6,chatbot:[10,15,17,18,19,23,25,26,27,28],chatterbot:[1,2,6],check:[6,17],check_fil:19,child:[12,14],chong:1,chosen:4,claim:[15,17,18,19,23,25,26,27,28],classifi:[2,17],clear:7,cli:[13,15],clone:7,close:16,code:2,collect:[1,4,5,6],colorama:6,colour:6,com:[6,7,17,19,23],command:[4,7],common:17,commonli:[4,5],commun:4,companion:10,compar:5,compat:17,complet:[4,7,8],complex:8,comprehend:10,comprehens:10,comput:8,condit:[15,17,18,19,23,25,26,27,28],confid:[3,4,8],confidence_from_stat:4,config:[3,4,13,15],configmanag:19,configur:[0,4,7,9,10],connect:[15,16,17,18,19,23,25,26,27,28],consid:[4,10],consist:4,constant:[13,15],contain:[5,17],content:[0,9,13],continu:[1,10],contract:[15,17,18,19,23,25,26,27,28],contribut:1,contributor:1,convent:4,converst:2,convert:[6,13,15,16],convert_data_escaped_str:16,cooki:4,copi:[15,17,18,19,23,25,26,27,28],copyright:[15,17,18,19,23,25,26,27,28],core:[15,17,18,19,23,25,26,27,28],corpora:5,corpu:5,correspond:[12,14],cosine_similar:17,covid:[13,15],cpu:11,creat:[3,6,8,12,14],creatun:1,cry:17,cry_overflow:17,currenc:6,currencyconvert:6,current:[7,17],current_tim:17,custom:6,damag:[15,17,18,19,23,25,26,27,28],darwin:[11,13,15],data:[3,6,7,9,16],databas:[0,3,7,9,10,16],database_path:16,dataset:[0,2,3,4,9],dead:17,deal:[15,17,18,19,23,25,26,27,28],debug:[4,12,13,14,15],defin:17,depend:[0,3,5,9],deploi:10,depress:17,depth:7,desktop:4,despit:4,dest:17,detail:[7,19,23],dev:3,develop:[1,10],differ:[4,17],differenti:1,dir:[12,14],direct:8,directori:3,dis:[13,15],discord:[4,10],displac:8,distanc:8,distribut:[8,15,17,18,19,23,25,26,27,28],diverg:2,django:6,document:[1,10,15,17,18,19,23,25,26,27,28],doesn:[12,14],dolik:[13,15],done:4,dotenv:6,download:[3,4,6],dure:4,dynam:[12,14],each:[12,14],easi:[1,7],easier:4,educ:10,effici:8,either:[12,13,14,15,19,23],email:10,emoji:6,emot:[13,15],en_core_web_md:1,en_core_web_sm:[1,6],encyclopedia:2,end:[3,8],engin:6,english:5,enter:4,entri:16,etc:5,even:[19,23],event:[15,17,18,19,23,25,26,27,28],exagger:5,exampl:[4,5,16],except:[12,14,16],exclud:[12,14],execut:[0,9],exist:[8,12,14,17],expand:17,experiment:17,explicit:[12,14],explicitli:4,explos:[1,2,6],express:[15,17,18,19,23,25,26,27,28],extend:[1,10],extract:5,fals:[8,17],famili:1,fault:[0,9],feel:[13,15],fetch:[5,11],few:[5,7],file:[3,4,5,6,10,15,17,18,19,23,25,26,27,28],filenam:20,find:5,first:[4,12,14,17],fit:[15,17,18,19,23,25,26,27,28],fix:17,folder:4,follow:[7,15,17,18,19,23,25,26,27,28],foobar:4,foolish:5,forev:10,form:[12,14,16,17],format:16,foundat:[19,23],framework:10,free:[2,6,10,15,17,18,19,23,25,26,27,28],freegam:6,frequenc:11,fresh:3,friend:1,from:[3,6,7,9,11,12,14,15,16,17,18,19,23,25,26,27,28],frontend:4,fun:[13,15],furnish:[15,17,18,19,23,25,26,27,28],futur:[3,10],game:[6,13,15],game_fil:20,gci:1,gen_arithmet:17,gen_best_match:17,gen_tim:17,gener:[10,19,23],geni:17,get:[5,6,7,12,14,18,19,23],get_cfgpath:19,get_config:19,git:7,github:[2,6,7,17,19,23],give:[5,6,8],given:17,globe:1,gnu:[4,19,23],gonzal:1,googl:[2,3,6,13,15],googlesearch:6,googletran:6,grant:[15,17,18,19,23,25,26,27,28],graphic:[7,10],gratitud:1,greater:11,gui:[13,15],guiscrcpi:[19,23],gunthercox:[1,2],handl:6,hangman:[13,15],hardwar:9,has:[1,4,8,10,12,14],hasanah:1,have:[4,5,8,19,23],headlin:6,help:[1,4,5,10],here:4,herebi:[15,17,18,19,23,25,26,27,28],hidden:4,higher:4,highli:10,holder:[15,17,18,19,23,25,26,27,28],hope:[19,23],host:[1,4,10],hour:17,howev:[4,5,10],html:6,http:[2,6,7,17,19,23],iam:[13,15],idk:[13,15],ignor:5,imit:[13,15],imper:5,impli:[15,17,18,19,23,25,26,27,28],in_reponse_to:16,includ:[5,7,15,17,18,19,23,25,26,27,28],incorrect:8,increas:5,increment:23,index:[0,2],industri:2,inflect:6,inform:5,initi:[10,17],inject:16,input:[3,10],insensit:4,instal:[8,11],instanc:[4,12,14],instead:[12,14],instruct:7,integ:17,intel:11,intelig:[15,18,19,23,25,27],intellig:[10,15,17,18,26,28],interact:4,interest:[5,10],interfac:[4,7,10],internet:11,interrog:5,interrupt:[13,15],introduct:0,intuit:10,invalid:9,investig:9,irc:10,isinst:[12,14],isn:[12,14],issu:[8,10],item:[12,14,17],iter:[12,14,17],its:[4,5,10],javascript:3,jensen:2,jia:4,joel:1,joke:[13,15],joshi:1,json:[3,4],just:7,keep:4,keyword:[3,12,14],kind:[15,17,18,19,23,25,26,27,28],kiy4h:1,known:5,lab:1,languag:[1,2,5,6,8,10],languageprocessor:17,later:[3,19,23],launch:7,launcher:[0,13],lead:8,learn:[1,2,3,10,13,15],lemma:[5,17],lemma_in:17,lend:10,less:4,lesser:4,let:[13,15],liabil:[15,17,18,19,23,25,26,27,28],liabl:[15,17,18,19,23,25,26,27,28],librari:[1,5],licens:[15,17,18,19,23,25,26,27,28],lies:5,like:[1,4,5,8,17],limit:[15,17,18,19,23,25,26,27,28],line:4,linguist:1,linux:[3,4,7,11,13,15],list:[4,5,12,14,17],liter:17,local:[4,7,17],logic:6,lol:17,low:3,lst1:17,lst2:17,lxml:6,mac:[3,7],machin:[1,2,10],magan:1,magic:[12,14],mai:[3,5,7,8],main:[4,17,25],make:[1,5,10],make_config:23,manag:[7,10],mani:5,manipul:[10,16],manual:4,marcu:1,mariadb:4,markdown:[13,15],mathew:1,mean:5,member:[12,14],memori:11,mention:1,merchant:[15,17,18,19,23,25,26,27,28],merg:[15,17,18,19,23,25,26,27,28],messag:10,method:[12,14],mhz:11,mic:[13,15],microphon:11,microsoft:[1,4,10],might:[3,5,8],million:1,minimum:11,minut:17,miss:1,mit:[15,17,18,19,23,25,26,27,28],mock:[12,14],mode:[4,19],model:6,modifi:[15,17,18,19,23,25,26,27,28],modul:[0,4,13],modular:10,mood:5,more:[1,4,5,7,19,23],most:[4,5,10],mover:8,much:4,multipl:[8,16],mynam:[13,15],mysql:[4,16],naiv:[2,4],naive_bayes_classifi:2,name:[12,14,16,20],natur:[1,2,4,5,8,10],necess:3,necessari:[6,10],need:4,neg:[5,17],negat:5,neglect:8,net:8,network:10,neural:10,neuron:17,neutral:17,new_conf:19,newsapi:6,next:[12,14],nlp:[4,10],nltk:[5,6,17],non:10,non_express:17,non_expressive_left:17,non_punkt_norm:17,none:[12,14],noninfring:[15,17,18,19,23,25,26,27,28],normal:[4,17],notat:3,note:4,notic:[15,17,18,19,23,25,26,27,28],number:17,numword:17,object:[3,10,12,14,15,16,17,18,19,23,25,27],obtain:[15,17,18,19,23,25,26,27,28],obvious:4,one:5,oneword:[13,15],onli:[1,4],ooo:[13,15],open:[1,4,10],oper:[4,17],option:[11,12,14,19,23],order:3,org:[2,19,23],organ:10,orient:10,other:[4,6,8,15,17,18,19,23,25,26,27,28],otherwis:[15,17,18,19,23,25,26,27,28],out:[5,10,15,17,18,19,23,25,26,27,28],overrid:8,packag:[0,2,7,13],page:0,paper:2,param:17,paramet:17,pars:17,part:1,particular:[15,17,18,19,23,25,26,27,28],particularli:[1,3,10],pass:[3,7,12,14],path:[3,4,7,11,16,23],path_to_db:16,path_to_local_databas:15,patron:10,peopl:4,permiss:[15,17,18,19,23,25,26,27,28],permit:[15,17,18,19,23,25,26,27,28],persist:[3,7],person:[10,15,17,18,19,23,25,26,27,28],pidddgi:1,pie:[1,7],pip:11,plai:[6,13,15],plan:10,platform:[4,6,13,15],polar:5,polici:9,popular:5,portabl:4,portion:[15,17,18,19,23,25,26,27,28],pos_in:17,posit:[5,17],possibl:[1,4,5,16],possiblesqlinjectionpanicerror:16,postprocessor:[13,15],powershel:7,pranav:2,prebuilt:9,precis:5,predict:8,prefer:11,preprocess:17,preprocessor:[13,15],present:3,press:10,prevent:4,preview:10,print:6,privaci:9,probabl:[3,8,10,17],problem:4,process:[1,2,5,6,8,10,17],processing_tim:16,processor:[6,11],product:[4,5,10],profit:10,program:[10,19,23],project:[1,2,10,15,17,18,19,23,25,26,27,28],prompt:4,prompt_cli:25,pronoun:17,propag:[12,14],proper:[4,6],properti:16,provid:[4,5,6,10,15,17,18,19,23,25,26,27,28],publish:[15,17,18,19,23,25,26,27,28],punctuat:5,purifi:17,purpos:[4,15,17,18,19,23,25,26,27,28],put:18,pyinflect:6,pypi:2,pyspellcheck:6,python:[2,5,6,7,10,11],pytorch:8,question:[2,3,4,6,17],rais:[8,12,14,16],raj:1,rajpurkar:[2,4],ram:11,random:17,random_respons:17,rather:[12,14],raw_in:17,raw_lower_in:17,read:[3,4],read_fil:19,reader:[10,13,15],readthedoc:2,real:[12,14],receiv:[19,23],recognit:[2,11],recommend:11,rectifi:1,redistribut:[19,23],reduc:8,refin:4,relat:3,releas:[3,6],remain:[5,10],remov:[3,17],repeat:1,replac:17,repli:5,repons:4,report:1,repositori:[2,8],repr:[12,14],repres:20,request:6,requir:[0,6,8,9,17],rereversei:[13,15],research:2,reset:[3,13,15,25],reset_config:19,reset_trivia:[13,15],respect:[4,5],respons:[1,3,4,7,9,10,17],restrict:[15,17,18,19,23,25,26,27,28],result:[5,6,8,11,12,14],retrain:3,return_typ:17,return_valu:[12,14],revers:17,reversethink:[13,15],rich:17,right:[15,17,18,19,23,25,26,27,28],rishikesh:1,riyaz:1,robot:5,root:5,rst:[13,15],rtype:16,run:[4,7],runserv:7,safe:4,saju:[1,15,17,18,19,23,25,26,27,28],same:[5,12,14],sampl:3,sashreek:1,save:[3,4],scan:17,score:5,scratch:3,scrawl:[13,15],screen:7,sdziuda:1,search:[0,6],second:17,see:[4,7,12,14,19,23],select:17,self:[4,10],sell:[15,17,18,19,23,25,26,27,28],semicolon:16,sens:5,sensit:4,sentiment:5,sequel:4,serious:17,serv:[3,10],server:[1,3,7,10],set:[12,14,17],setup:[0,13],sever:[12,14],shall:[15,17,18,19,23,25,26,27,28],shannon:2,should:[7,8,19,23],show:4,side_effect:[12,14],sigmasimilar:17,similar:[8,17],simpler:5,singl:4,size:8,sleep:17,smag:1,smile:10,smirk:17,softwar:[9,10,15,17,18,19,23,25,26,27,28],sole:3,solv:4,some:[3,4,5,7],sometim:[5,8],sourc:[1,2,4,10,15,16,17,18,19,20,23,25,27],spac_token:17,spaci:[1,2,5,6,8],spacy_token:17,spec:[12,14],spec_set:[12,14],special:1,specif:[12,14],specifi:[12,14],speech:[2,3,5,11],speechrecognit:2,spell:6,sponsor:[1,10],sql:[4,13,15],sqldatabasemanag:16,sqlite3:9,sqlite:3,squad:4,squad_train:[13,15],src:17,srevin:[15,17,18,19,23,25,26,27,28],srevinsaju:[4,7,19,23],sreya:1,sreyasaju:1,sruthi:1,stabl:[2,3],stackoverflow:17,stanford:[2,4],start:[4,7],statement:[5,16,17],statment:5,statu:7,still:[4,10],stopword:5,store:[3,4,7],str:[16,17],strength:2,stricter:[12,14],string1:17,string:[12,14,16,17],string_arg:17,stype:17,subject:[15,17,18,19,23,25,26,27,28],sublicens:[15,17,18,19,23,25,26,27,28],submodul:13,subpackag:13,substanti:[15,17,18,19,23,25,26,27,28],sugar:[1,5],sugarlab:10,sugaroid:[1,3,4,5,6,7,8,9],sugaroid_hist:16,sugaroid_intern:[3,4],sugaroidcliwrapp:18,sugaroidtrain:[15,25],sugaroidtrivia:27,suitabl:8,superl:5,supervis:9,support:[7,10],swaglyr:[13,15],swap:11,system:[3,4,8,23],szymon:1,tabl:16,tackl:10,tackler:8,take:[5,12,14],tamper:4,tar:6,target:16,teach:4,team:1,tensor:8,tensorflow:8,term:[5,19,23],termin:7,test:[1,4,10,12,14,17],text2int:17,text:[3,5,6,17],textnum:17,than:[11,12,14],thank:[1,10],thedarkdrak:1,thei:[4,12,14],them:3,thi:[1,3,4,8,10,12,14,15,17,18,19,23,25,26,27,28],thing:5,three:10,through:[4,12,14],time:[5,8,13,15,16],token:17,tone:5,tort:[15,17,18,19,23,25,26,27,28],train:[0,3,5,6,7,9,13,25],trainer:[3,4,7,13,15],trainer_cli:25,trainer_init:25,translat:[1,6,13,15],triag:1,trivia:[13,15],triviadb:[13,15],tts:[13,15],tupl:[16,17],two:4,twoword:[13,15],txt:17,type:[3,4,17],under:[10,19,23],undergo:4,understand:5,uniqu:5,unix:4,unknown:8,unless:[12,14],unsupervis:9,unsupport:[12,14],unwant:17,updat:[7,13,15],update_config:19,use:[7,15,17,18,19,23,25,26,27,28],used:[3,4,5,6,12,14],useful:[4,5,12,14,19,23],user:[3,4,6,7,8,10],usernam:3,uses:[3,4,5,8,10],util:[10,13,15],vader_lexicon:5,valu:[8,12,14,17],valueerror:16,variant:[12,14],varieti:17,vector:[5,8],veri:[4,5],versa:17,version:[4,11,13,19,23],vice:17,virtual:10,vomit:17,wai:[4,17],waitwhat:[13,15],warranti:[15,17,18,19,23,25,26,27,28],web:[2,4,7,10],webpag:6,websit:2,well:[5,8],what:[5,8],whatamido:[13,15],whatwhat:[13,15],when:[4,10,12,14],whenev:[3,12,14],where:[3,4],whether:[15,17,18,19,23,25,26,27,28],which:[1,3,4,5,6,7,8,10,17],who:1,whoami:[13,15],whom:[15,17,18,19,23,25,26,27,28],why:[13,15],wide:10,wiki:[2,13,15],wikipedia:[2,6,11],willing:10,window:[3,4,7,11,13,15],wink:17,within:16,without:[5,15,17,18,19,23,25,26,27,28],wolfalpha:[13,15],word:[1,5,6,8,17],word_token:17,work:1,world:10,would:[1,4,8,17],wrap:[12,14],write:25,write_fil:19,wrong:5,wsgi:7,www:[19,23],x_list:17,xml:6,y_list:17,yesno:[13,15],you:[4,7,10,12,14,17,19,23],your:[3,4,7,10,19,23],zakiyah:1,zero:8,zip:5},titles:["Welcome to Sugaroid\u2019s documentation!","Acknowledgements","Bibliography","Configuration","Databases and Training","Datasets","Dependencies","Execution","Faults","Introduction","Sugaroid","Requirements","launcher module","sugaroid","setup module","sugaroid package","sugaroid.backend package","sugaroid.brain package","sugaroid.cli package","sugaroid.config package","sugaroid.game package","sugaroid.google package","sugaroid.gui package","sugaroid.platform package","sugaroid.reader package","sugaroid.trainer package","sugaroid.translator package","sugaroid.trivia package","sugaroid.tts package"],titleterms:{"new":17,about:17,acknowledg:1,aki:17,arey:17,assert:17,backend:16,becaus:17,bibliographi:2,brain:17,bye:17,canmai:17,cli:18,config:19,configur:3,constant:17,content:[15,16,17,18,19,20,21,22,23,24,25,26,27,28],convert:17,covid:17,darwin:23,data:4,databas:4,dataset:5,debug:17,depend:6,dis:17,document:0,dolik:17,either:17,emot:17,execut:7,fault:8,feel:17,from:4,fun:17,game:20,googl:21,gui:22,hangman:17,hardwar:11,iam:17,idk:17,imit:17,indic:0,interrupt:17,introduct:[9,10],invalid:8,investig:4,joke:17,launcher:12,learn:17,let:17,lexicon:5,linux:23,markdown:24,mic:28,modul:[12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],mynam:17,oneword:17,ooo:17,packag:[15,16,17,18,19,20,21,22,23,24,25,26,27,28],plai:17,platform:23,polici:4,postprocessor:17,prebuilt:5,preprocessor:17,privaci:4,punkt:5,reader:[17,24],requir:11,rereversei:17,reset:17,reset_trivia:17,respons:8,reversethink:17,rst:24,scrawl:24,setup:14,softwar:11,sql:16,sqlite3:4,squad_train:25,submodul:[15,16,17,18,19,20,21,22,23,24,25,26,27,28],subpackag:15,sugaroid:[0,10,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28],supervis:4,swaglyr:17,tabl:0,time:17,train:[4,15],trainer:25,translat:26,trivia:[17,27],triviadb:27,tts:28,twoword:17,unsupervis:4,updat:17,util:17,vader:5,version:15,waitwhat:17,welcom:0,whatamido:17,whatwhat:17,whoami:17,why:17,wiki:17,window:23,wolfalpha:17,wordnet:5,yesno:17}})