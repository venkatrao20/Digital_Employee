import { useState } from 'react';
import {
  Pressable,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  View,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const colors = {
  ink: '#202522',
  muted: '#6F766D',
  paper: '#F4F1EA',
  white: '#FFFDF8',
  sage: '#A8B7A0',
  sageDark: '#445748',
  coral: '#D46F55',
  line: '#DDD9D0',
};

const starterRequirement =
  'Customers need a simple way to save a draft order and resume it later.';

type Analysis = {
  summary: string;
  stories: string[];
  risks: string[];
  questions: string[];
};

function analyzeRequirement(input: string): Analysis {
  const normalizedInput = input.toLowerCase();
  const isCartRequirement = normalizedInput.includes('cart') || normalizedInput.includes('shopping');

  if (isCartRequirement) {
    return {
      summary: 'A shopping cart flow that lets customers manage products and review the total before checkout.',
      stories: [
        'As a customer, I want to add products to my cart so I can purchase them together.',
        'As a customer, I want to change product quantities so I can adjust my order.',
        'As a customer, I want to remove products so I can correct my order before checkout.',
        'As a customer, I want to see the cart total so I know the expected price.',
      ],
      risks: ['Price and inventory may change while products remain in the cart.', 'The cart total must handle quantity, discounts, tax, and currency rules consistently.'],
      questions: ['Should the cart persist for returning customers?', 'Should customers be able to check out with an empty cart?'],
    };
  }

  return {
    summary: 'A customer requirement that needs product and delivery details clarified before implementation.',
    stories: [`As a customer, I want the following need supported: ${input.trim()}`],
    risks: ['The expected business rules and edge cases are not fully defined.'],
    questions: ['What is the desired outcome for the customer?', 'What rules, limits, or error states should the experience support?'],
  };
}

export default function App() {
  const [requirement, setRequirement] = useState('');
  const [analysis, setAnalysis] = useState<Analysis | null>(null);
  const [activeTab, setActiveTab] = useState<'capture' | 'history'>('capture');
  const [isRunning, setIsRunning] = useState(false);

  function runAnalysis() {
    if (!requirement.trim() || isRunning) return;
    setIsRunning(true);
    setTimeout(() => {
      setAnalysis(analyzeRequirement(requirement));
      setIsRunning(false);
    }, 650);
  }

  function useStarter() {
    setRequirement(starterRequirement);
    setAnalysis(null);
    setActiveTab('capture');
  }

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" />
      <ScrollView contentContainerStyle={styles.page} keyboardShouldPersistTaps="handled">
        <View style={styles.header}>
          <View>
            <Text style={styles.eyebrow}>BA FIELD NOTES</Text>
            <Text style={styles.title}>Turn loose ideas into{`\n`}clear next steps.</Text>
          </View>
          <View style={styles.mark}>
            <Ionicons name="sparkles" size={21} color={colors.white} />
          </View>
        </View>

        <View style={styles.tabs}>
          <Pressable style={[styles.tab, activeTab === 'capture' && styles.activeTab]} onPress={() => setActiveTab('capture')}>
            <Ionicons name="create-outline" size={17} color={activeTab === 'capture' ? colors.ink : colors.muted} />
            <Text style={[styles.tabText, activeTab === 'capture' && styles.activeTabText]}>Capture</Text>
          </Pressable>
          <Pressable style={[styles.tab, activeTab === 'history' && styles.activeTab]} onPress={() => setActiveTab('history')}>
            <Ionicons name="time-outline" size={17} color={activeTab === 'history' ? colors.ink : colors.muted} />
            <Text style={[styles.tabText, activeTab === 'history' && styles.activeTabText]}>History</Text>
          </Pressable>
        </View>

        {activeTab === 'capture' ? (
          <>
            <View style={styles.introRow}>
              <View>
                <Text style={styles.sectionLabel}>NEW ANALYSIS</Text>
                <Text style={styles.sectionTitle}>What are you hearing?</Text>
              </View>
              <View style={styles.stepBadge}><Text style={styles.stepText}>01 / 01</Text></View>
            </View>

            <Text style={styles.helper}>Paste a customer requirement, meeting note, or rough idea. The BA team will shape it into something actionable.</Text>
            <View style={styles.inputWrap}>
              <TextInput
                multiline
                value={requirement}
                onChangeText={setRequirement}
                placeholder="Customers need..."
                placeholderTextColor="#9CA198"
                style={styles.input}
                textAlignVertical="top"
              />
              <Text style={styles.counter}>{requirement.length} / 1000</Text>
            </View>

            <Pressable style={({ pressed }) => [styles.primaryButton, pressed && styles.pressed, (!requirement.trim() || isRunning) && styles.disabled]} onPress={runAnalysis}>
              <Text style={styles.primaryButtonText}>{isRunning ? 'Working through it...' : 'Run BA analysis'}</Text>
              <Ionicons name={isRunning ? 'hourglass-outline' : 'arrow-forward'} size={19} color={colors.white} />
            </Pressable>

            {!analysis && <Pressable style={styles.exampleRow} onPress={useStarter}>
              <View style={styles.exampleIcon}><Ionicons name="bulb-outline" size={18} color={colors.coral} /></View>
              <View style={styles.exampleCopy}><Text style={styles.exampleLabel}>TRY AN EXAMPLE</Text><Text style={styles.exampleText}>Save and resume a draft order</Text></View>
              <Ionicons name="arrow-up-outline" size={18} color={colors.muted} />
            </Pressable>}

            {analysis && <AnalysisView analysis={analysis} />}
          </>
        ) : (
          <View style={styles.emptyState}>
            <View style={styles.emptyIcon}><Ionicons name="archive-outline" size={25} color={colors.sageDark} /></View>
            <Text style={styles.sectionTitle}>Your analyses will live here.</Text>
            <Text style={styles.helper}>Run your first analysis to build a lightweight record of decisions, questions, and follow-ups.</Text>
            <Pressable style={styles.secondaryButton} onPress={() => setActiveTab('capture')}><Text style={styles.secondaryButtonText}>Start an analysis</Text></Pressable>
          </View>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

function AnalysisView({ analysis }: { analysis: Analysis }) {
  return <View style={styles.results}>
    <View style={styles.resultHeader}><View><Text style={styles.sectionLabel}>ANALYSIS READY</Text><Text style={styles.sectionTitle}>A clearer starting point.</Text></View><View style={styles.readyBadge}><Ionicons name="checkmark" size={15} color={colors.sageDark} /><Text style={styles.readyText}>Ready</Text></View></View>
    <View style={styles.summaryCard}><Text style={styles.cardLabel}>REQUIREMENT SUMMARY</Text><Text style={styles.summaryText}>{analysis.summary}</Text></View>
    <ResultGroup icon="list-outline" title="User stories" items={analysis.stories} />
    <ResultGroup icon="warning-outline" title="Risks to explore" items={analysis.risks} />
    <ResultGroup icon="help-circle-outline" title="Clarification questions" items={analysis.questions} />
  </View>;
}

function ResultGroup({ icon, title, items }: { icon: keyof typeof Ionicons.glyphMap; title: string; items: string[] }) {
  return <View style={styles.group}><View style={styles.groupTitle}><Ionicons name={icon} size={18} color={colors.coral} /><Text style={styles.groupHeading}>{title}</Text></View>{items.map((item) => <View style={styles.item} key={item}><View style={styles.dot} /><Text style={styles.itemText}>{item}</Text></View>)}</View>;
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: colors.paper },
  page: { padding: 24, paddingBottom: 52 },
  header: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 28 },
  eyebrow: { color: colors.coral, fontSize: 11, fontWeight: '800', letterSpacing: 1.8, marginBottom: 10 },
  title: { color: colors.ink, fontSize: 30, lineHeight: 35, fontWeight: '800', letterSpacing: -0.5 },
  mark: { alignItems: 'center', backgroundColor: colors.sageDark, borderRadius: 16, height: 48, justifyContent: 'center', width: 48 },
  tabs: { borderBottomColor: colors.line, borderBottomWidth: 1, flexDirection: 'row', gap: 26, marginBottom: 30 },
  tab: { alignItems: 'center', flexDirection: 'row', gap: 7, paddingBottom: 12 },
  activeTab: { borderBottomColor: colors.coral, borderBottomWidth: 2 },
  tabText: { color: colors.muted, fontSize: 14, fontWeight: '600' },
  activeTabText: { color: colors.ink },
  introRow: { alignItems: 'center', flexDirection: 'row', justifyContent: 'space-between' },
  sectionLabel: { color: colors.muted, fontSize: 10, fontWeight: '800', letterSpacing: 1.4, marginBottom: 7 },
  sectionTitle: { color: colors.ink, fontSize: 21, fontWeight: '800' },
  stepBadge: { backgroundColor: '#E5E9DF', borderRadius: 99, paddingHorizontal: 10, paddingVertical: 6 },
  stepText: { color: colors.sageDark, fontSize: 10, fontWeight: '800', letterSpacing: 0.6 },
  helper: { color: colors.muted, fontSize: 14, lineHeight: 21, marginBottom: 18, marginTop: 13 },
  inputWrap: { backgroundColor: colors.white, borderColor: colors.line, borderRadius: 14, borderWidth: 1, minHeight: 164, padding: 16 },
  input: { color: colors.ink, flex: 1, fontSize: 16, lineHeight: 24, minHeight: 120 },
  counter: { alignSelf: 'flex-end', color: '#9CA198', fontSize: 11 },
  primaryButton: { alignItems: 'center', backgroundColor: colors.coral, borderRadius: 12, flexDirection: 'row', justifyContent: 'center', gap: 10, marginTop: 14, paddingVertical: 16 },
  primaryButtonText: { color: colors.white, fontSize: 15, fontWeight: '800' },
  pressed: { opacity: 0.82 },
  disabled: { opacity: 0.45 },
  exampleRow: { alignItems: 'center', borderBottomColor: colors.line, borderBottomWidth: 1, flexDirection: 'row', gap: 12, paddingVertical: 18 },
  exampleIcon: { alignItems: 'center', backgroundColor: '#F8E5DC', borderRadius: 10, height: 38, justifyContent: 'center', width: 38 },
  exampleCopy: { flex: 1 },
  exampleLabel: { color: colors.muted, fontSize: 9, fontWeight: '800', letterSpacing: 1.3, marginBottom: 3 },
  exampleText: { color: colors.ink, fontSize: 14, fontWeight: '600' },
  results: { marginTop: 33 },
  resultHeader: { alignItems: 'flex-start', flexDirection: 'row', justifyContent: 'space-between', marginBottom: 18 },
  readyBadge: { alignItems: 'center', backgroundColor: '#E1EBDD', borderRadius: 99, flexDirection: 'row', gap: 4, paddingHorizontal: 10, paddingVertical: 6 },
  readyText: { color: colors.sageDark, fontSize: 11, fontWeight: '800' },
  summaryCard: { backgroundColor: colors.sageDark, borderRadius: 14, marginBottom: 25, padding: 18 },
  cardLabel: { color: '#C6D1C2', fontSize: 10, fontWeight: '800', letterSpacing: 1.2, marginBottom: 10 },
  summaryText: { color: colors.white, fontSize: 16, fontWeight: '600', lineHeight: 24 },
  group: { borderBottomColor: colors.line, borderBottomWidth: 1, paddingBottom: 18, paddingTop: 2 },
  groupTitle: { alignItems: 'center', flexDirection: 'row', gap: 8, marginBottom: 12 },
  groupHeading: { color: colors.ink, fontSize: 16, fontWeight: '800' },
  item: { alignItems: 'flex-start', flexDirection: 'row', gap: 10, marginBottom: 9, paddingLeft: 3 },
  dot: { backgroundColor: colors.coral, borderRadius: 5, height: 6, marginTop: 7, width: 6 },
  itemText: { color: colors.muted, flex: 1, fontSize: 14, lineHeight: 20 },
  emptyState: { alignItems: 'center', paddingTop: 70 },
  emptyIcon: { alignItems: 'center', backgroundColor: '#E5E9DF', borderRadius: 18, height: 58, justifyContent: 'center', marginBottom: 18, width: 58 },
  secondaryButton: { borderColor: colors.sageDark, borderRadius: 10, borderWidth: 1, marginTop: 6, paddingHorizontal: 18, paddingVertical: 13 },
  secondaryButtonText: { color: colors.sageDark, fontSize: 14, fontWeight: '800' },
});