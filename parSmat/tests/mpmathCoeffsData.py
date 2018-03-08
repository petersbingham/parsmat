import pynumwrap as nw
TESTDPS = 40
nw.useMpmathTypes(TESTDPS)

sMatData = {nw.mpf('1.0'): nw.matrix([[nw.mpc(real='-0.9035061795881897271183573871099408926215',imag='0.4285750616239281985579964961941083103659'),  nw.mpc(real='1.35194964556261028295718440465645224833',imag='0.855044226986120550015062446068837955507')], [ nw.mpc(real='1.35194964556261028295718440465645224833',imag='0.855044226986120550015062446068837955507'), nw.mpc(real='-10.72907621655570403075417982784331447184',imag='-1.279434237119580005892120398441009444365')]]), 
            nw.mpf('2.4'): nw.matrix([[nw.mpc(real='-0.01514201102047645349961872516635962963436',imag='0.9362359060112529631344928051470581148755'),  nw.mpc(real='-0.2140505087155649231708634185540283542351',imag='-0.2782362800142209028684770156904336133757')], [ nw.mpc(real='-0.2140505087155649231708634185540283542351',imag='-0.2782362800142209028684770156904336133757'), nw.mpc(real='-0.9088190499507801981491861480368798369446',imag='-0.2254215753849156510585342449105225513031')]]), 
            nw.mpf('3.8'): nw.matrix([[nw.mpc(real='0.3593119421311074559187153514407596677341',imag='0.9008837188556393862019242796686922112187'),  nw.mpc(real='-0.2434775115655364060860096799788034630378',imag='0.00470687844107585299407183333696616022338')], [ nw.mpc(real='-0.2434775115655364060860096799788034630378',imag='0.00470687844107585299407183333696616022338'), nw.mpc(real='-0.3242249347133430959447483536161053534273',imag='0.9140977728707818200925590211775205495599')]]), 
            nw.mpf('5.2'): nw.matrix([[nw.mpc(real='0.5365338240950710076029910706000656059494',imag='0.8174280910049940711174183034291236373271'),  nw.mpc(real='-0.1924165629852158830688214362355503716335',imag='0.08317835010870906522841940368827483005237')], [ nw.mpc(real='-0.1924165629852158830688214362355503716335',imag='0.08317835010870906522841940368827483005237'), nw.mpc(real='0.227866378764338476736640057529269344276',imag='0.9508596856481909457786395032409728484883')]]), 
            nw.mpf('6.6'): nw.matrix([[nw.mpc(real='0.5958805413537130229584220171170289488045',imag='0.7761770204736209070218726738058860092364'),  nw.mpc(real='-0.1713242457959797978532641129979233045506',imag='0.1145583524983528811649474212729421755217')], [ nw.mpc(real='-0.1713242457959797978532641129979233045506',imag='0.1145583524983528811649474212729421755217'), nw.mpc(real='0.4896289877598058327198779550665046852377',imag='0.8472236074500106461205187256993810925549')]]),
            nw.mpf('8.0'): nw.matrix([[nw.mpc(real='0.6044289357883593355150693046832523858479',imag='0.7671257047686346758484610727241773341955'),  nw.mpc(real='-0.170024042876760909519335082245025263874',imag='0.1314368270646332394465398247692174346427')], [ nw.mpc(real='-0.170024042876760909519335082245025263874',imag='0.1314368270646332394465398247692174346427'), nw.mpc(real='0.5901530827564504021279275291622530481834',imag='0.7781616311847309694697491539879288442998')]])}

A = [nw.matrix([[nw.mpc(real='1.0',imag='0.0'), nw.mpc(real='0.0',imag='0.0')],
      [nw.mpc(real='0.0',imag='0.0'), nw.mpc(real='1.0',imag='0.0')]]),

    nw.matrix([[nw.mpc(real='-1.306389410705926837064012637598799299852',imag='-0.08538900278782996006897281030036024744349'), nw.mpc(real='0.2201680105110934593094017529140285739812',imag='-0.5114674425144446658696629210232535443511')],
      [nw.mpc(real='-0.7971299292276996570445401737294318150426',imag='-0.1065692888203888750134754445651110609121'), nw.mpc(real='-2.128743826970827071193898571530299389051',imag='0.921492524848920041075585913125123424885')]]),

    nw.matrix([[nw.mpc(real='0.4381246407334317212939039521843318738638',imag='0.01974187626971263048102264545065395255536'), nw.mpc(real='0.03270147842506364139426393929993331240709',imag='0.01299615721478474092959413589082636284089')],
      [nw.mpc(real='0.3264714394177256857180863596960015900612',imag='0.05123681631129223128386594754718042740392'), nw.mpc(real='0.721563582473320789310044294536532786998',imag='-0.2716301892278420795064147376744328510023')]]),

    nw.matrix([[nw.mpc(real='-0.02916561205815645202532224840368732565355',imag='-0.01925169854371813726809742510153695274338'), nw.mpc(real='0.2672116420588423707019430981565374030731',imag='-0.3513841333523345980057218629463542270979')],
      [nw.mpc(real='-0.005997607134803133471857809453063312440331',imag='-0.001031646278609318696371817524730149282143'), nw.mpc(real='-0.05124932370627698168584011973090335159131',imag='0.01190143749481226156922769553755199805665')]])]

B = [nw.matrix([[nw.mpc(real='0.0',imag='0.0'), nw.mpc(real='0.0',imag='0.0')],
      [nw.mpc(real='0.0',imag='0.0'), nw.mpc(real='0.0',imag='0.0')]]),

    nw.matrix([[nw.mpc(real='0.05650518229291723118354273115413341421698',imag='-0.07296216434884201546985295906508476336693'), nw.mpc(real='1.159713642354759441557259860685951760223',imag='-1.528392435327927013600446286276242247152')],
      [nw.mpc(real='0.4900279284791779145061707233581351724147',imag='0.05639652705485429634167718787593608961078'), nw.mpc(real='0.812927902683429674794386026049658872971',imag='-0.7229939398569022530293016620556636938638')]]),

    nw.matrix([[nw.mpc(real='0.01602458365357923595246945079647084609451',imag='0.0112847183489553018814977416639704408516'), nw.mpc(real='-0.145248613838481202005838880355464787706',imag='0.2039895863773912206341201212110367244617')],
      [nw.mpc(real='-0.06946866312898202642484097658853112730395',imag='-0.007130332347564192860895960950661909912147'), nw.mpc(real='-0.1379764512130805152078904678778144138973',imag='0.1352384502937413748365527190188984914539')]]),

    nw.matrix([[nw.mpc(real='-0.001133549395178496202759157564014850598265',imag='-0.002356384071415779957018190971797467436703'), nw.mpc(real='0.03415908253385076528933320936238248143731',imag='-0.04596193622342289214781131591230779812676')],
      [nw.mpc(real='0.004520013551082494566243379651103957295515',imag='-0.00006353364400204682077902560603880014269325'), nw.mpc(real='0.01494985900266205717937412932136852729121',imag='-0.0188233570624465091709844826590596335601')]])]
